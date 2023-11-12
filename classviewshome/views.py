from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ArticleForm, BookForm, CustomUserCreationForm
from .models import *
class HomeView(TemplateView):
    template_name = 'classviewshome/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_date'] = 'Доп информация'
        return context

# def homeView(request):
#     return render(request, 'home/home.html', {'custom_date': Доп информация})
# это было бы без класса

class ArticleListView(ListView):
    model = Article  #  articles = Article.objects.all()
    # context_object_name = 'article'
    # template_name = 'classviewshome/article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_books'] = Book.objects.filter(article=self.object)
        return context

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    success_url = '/articles/'

class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    success_url = '/articles/'

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = '/articles/'

class BookListView(ListView):
    model = Book

class BookDetailView(DetailView):
    model = Book

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    success_url = '/books/'

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    success_url = '/books/'
class BookDeleteView(DeleteView):
    model = Book
    success_url = '/books/'

class UserCreateView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'classviewshome/register.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.full_name = form.cleaned_data['full_name']
        user.birth_date = form.cleaned_data['birth_date']
        user.save()
        login(self.request, user)
        return super().form_valid(form)

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'classviewshome/profile.html'

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context