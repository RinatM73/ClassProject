from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name = 'classviewshome'),
    path('blog/', BlogView.as_view(), name = 'blog')
]