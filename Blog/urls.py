"""
URL configuration for BlogConfig project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from .views import *

app_name = 'Blog'

urlpatterns = [
    # Ruta para la lista de todos los posts (página principal del blog)
    path('', PostListView.as_view(), name='post_list'),
    # Ruta para Mostar por categoria
    path('category/<str:category_name>/', PostListView.as_view(), name='posts_by_category'), # Para filtrar por categoría
    # Ruta para crear un nuevo post
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    # Ruta para los detalles de un post específico, usando su slug
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    # Ruta para editar un post existente, usando su slug
    path('post/<slug:slug>/edit/', PostUpdateView.as_view(), name='post_edit'),
    # Ruta para eliminar un post existente, usando su slug
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),

    path('signup/', SignUpView.as_view(), name='signup'),

]