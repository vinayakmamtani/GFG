from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = "home"),
    path("signup",views.home,name = "signup"),
    path('signin',views.home,name = "signin"),
    path('signout',views.home,name = "signout"),
]
