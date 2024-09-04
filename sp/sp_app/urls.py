"""sp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
#urls for the paths

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from sp import settings
from sp_app import views

urlpatterns = [
    path('', views.ab, name='home'),
    path('abc/', views.abc, name='abc'),
    path('addfile/', views.addfile, name='addfile'),
    path('addfilepost/', views.addfilepost, name='addfilepost'),
    path('login/', views.login, name='login'),
    path('login_post/', views.login_post, name='login_post'),
    path('user_register/', views.user_register, name='user_register'),
    path('user_register_POST/', views.user_register_POST, name='user_register_POST'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)