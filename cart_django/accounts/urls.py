from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='loginPage'),
    path('check_login/', views.checklogin, name='checklogin'),
    path('logout/', views.logoutPage, name='logoutPage'),
    path('register/', views.registerPage, name='registerPage'),
]