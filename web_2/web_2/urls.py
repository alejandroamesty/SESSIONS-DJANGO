"""
URL configuration for web_2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from sessions_component.views import login, logout, changepassword, signup, checkpermissions, unregister, process, forgotpassword

urlpatterns = [
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('change-password', changepassword, name='change-password'),
    path('signup', signup, name='signup'),
    path('check-permissions', checkpermissions, name='check-permissions'),
    path('unregister', unregister, name='unregister'),
    path('process', process, name='process'),
    path('forgotpassword', forgotpassword, name='forgotpassword'),
]
