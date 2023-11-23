from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=250, verbose_name="ФИО", blank=True, null=True)
    birth_date = models.DateField(verbose_name="Дата рождения", blank=True, null=True)
    image_profile = models.ImageField(upload_to='profile/image/', verbose_name='Фото профиля')
    about_me = models.TextField(verbose_name='О себе', blank=True)

class Team(models.Model):
    first_name = models.CharField(max_length=250, verbose_name="Имя", blank=True, null=True)
    second_name = models.CharField(max_length=250, verbose_name="Фамилия", blank=True, null=True)
    image_profile1 = models.ImageField(upload_to='image', verbose_name='Фото профиля')
    your_country = models.CharField(max_length=250, verbose_name="Страна", blank=True, null=True)
    your_city = models.CharField(max_length=250, verbose_name="Город", blank=True, null=True)

    def __str__(self):
        return f"{self.first_name}, {self.second_name}"

class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")

    def __str__(self):
        return f"{self.title}, {self.text}"

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.CharField(max_length=340, verbose_name="Описание")
    article = models.ManyToManyField(Article, verbose_name="Статьи")

    def __str__(self):
        return f"{self.title}, {self.article}"