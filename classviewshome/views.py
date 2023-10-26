from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import *
class HomeView(TemplateView):
    template_name = 'classviewshome/article_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_date'] = 'Доп информация'
        return context

# def homeView(request):
#     return render(request, 'home/home.html', {'custom_date': Доп информация})
# это было бы без класса

class BlogView(ListView):
    model = Article  #  articles = Article.objects.all()

    #template_name = 'classviewshome/article_list.html'
