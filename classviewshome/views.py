from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ArticleForm, BookForm
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
    form_class = BookForm
    success_url = '/books/'