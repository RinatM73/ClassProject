from django.contrib.auth.views import LoginView
from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('articles/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('create_article/', ArticleCreateView.as_view(), name='create_article'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('create_book/', BookCreateView.as_view(), name='create_book'),
    path('update_book/', BookUpdateView.as_view(), name='update_book'),
    path('delete_book/', BookDeleteView.as_view(), name='delete_book'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),

]