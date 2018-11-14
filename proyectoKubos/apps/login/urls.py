from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views 
urlpatterns = [
    path('prebes/',include("apps.prebes.urls")),
    path('',auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('registrate/',views.registrate,name="registrate"),
]
