"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .import index
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.signup, name='signup'),
    path('home', index.home, name='home'),
    path('login/', index.login, name='login'),
    path('logout_user', index.logout_user, name='logout'),
    path('chat', views.chat_view, name='chat'),
    path('ambulance', index.ambulance, name='ambulance'),
    path('hospital', index.hospital, name='hospital'),
    path('pharmacy', index.pharmacy, name='pharmacy'),
    path('bloodbank', index.bloodbank, name='bloodbank')

]
