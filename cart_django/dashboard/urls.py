from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('product_view/<int:id>', views.product_view, name='product_view'),
    path('product_add/', views.product_add, name='product_add'),
    path('product_edit/<int:id>', views.product_edit, name='product_edit'),
    path('product_delete/<int:id>', views.product_delete, name='product_delete'),
    path('statistical', views.statistical, name='statistical'),
]