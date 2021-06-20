from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    # Схема домашней страницы.
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    # Схема добавления нового сообщения.
    path('new_blog_post/', views.new_blog_post, name='new_blog_post'),
    # Схема сообщения.
    path('blog_post/<int:blog_post_id>', views.blog_post, name='blog_post'),
    # Схема для редактирования сообщения.
    path('edit_blog_post/<int:blog_post_id>', views.edit_blog_post,
         name='edit_blog_post'),
]
