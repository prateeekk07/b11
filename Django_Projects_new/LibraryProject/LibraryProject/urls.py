"""LibraryProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from book.views import welcome , create_book , edit_book , delete_book , show_deleted_books , restore_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', welcome, name="home"),
    path('add-book/', create_book, name="add_book"),
    path('edit-book/<int:bid>/', edit_book, name="edit_book"),
    path('delete-book/<int:bid>/', delete_book, name="delete_book"),
    path('deleted-books/', show_deleted_books, name="show_deleted_books"),
    path('restore-book/<int:bid>/', restore_book, name="restore_book"),
    path('user/', include('user_app.urls')), #include all the urls from user_app


]
