from django.urls import path
from . import views

urlpatterns = [
    path('product_home/', views.product_home, name='product_home'),
    
]