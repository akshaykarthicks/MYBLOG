from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.post, name='post'),#this is used to pass the post id to the post view for diff post
    path('create/', views.create_post, name='create_post'),
    
]

