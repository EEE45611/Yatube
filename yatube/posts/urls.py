from . import views
from django.urls import path
urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('posts', views.posts),
    path('register', views.register),
    path('login', views.login),
]
