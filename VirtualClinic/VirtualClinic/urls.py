"""VirtualClinic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from appointment.views import *
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', book),
    path('register/', register),
    path('login/', login),
    path('find_doctor/', find_doctor),
    path('approve/', approve),
    path('disease/', views.index, name = 'index'),
    path('predictdis/', views.predictdis, name = 'predictdis'),
    path('details/',views.details, name = 'details')

]
