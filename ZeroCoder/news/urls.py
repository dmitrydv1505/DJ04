from django.urls import path, include
from . import views

urlpatterns = [
#    path('', views.home, name='news_home'),
    path('news/', views.news, name='news'),
    path('news_home/', views.home, name='news_home'),
    path('create_news/', views.create_news, name='add_news'),
]