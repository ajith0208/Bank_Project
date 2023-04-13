from django.contrib import admin
from django.urls import path, include
from bankapp import views
app_name = 'bankapp'
urlpatterns = [
    path("", views.body, name='home'),
    path("login", views.login, name='login'),
    path("logout", views.logout, name='logout'),
    path("register", views.register, name='register'),
    path("apply/", views.apply, name='apply'),
    path("new", views.new, name='new'),



]


