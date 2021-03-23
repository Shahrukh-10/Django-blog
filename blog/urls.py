from django.urls import path,include
from . import views

urlpatterns = [
        path('', views.blog , name = 'Blog'),
        path('postComment', views.postComment , name='PostComment'),
        path('<str:slug>', views.blogpost , name='BlogPost'),
]