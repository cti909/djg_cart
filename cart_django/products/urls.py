from django.urls import path
from . import views

urlpatterns = [
    path('product_home/', views.product_home, name='product_home'),
    path('product_category/<str:category>', views.product_category, name='product_category'),
    # path('product_add/', views.product_add, name='product_add'),
    path('product_detail/<int:id>', views.product_detail, name='product_detail'),
    # path('product_edit/<int:id>', views.product_edit, name='product_edit'),
    # path('product_delete/<int:id>', views.product_delete, name='product_delete'),
    path('product_search/', views.product_search, name='product_search'),
    path('product_sort/', views.product_sort, name='product_sort'),
    # path('product_detail/(?P<id>[0-9]+)$', views.product_detail, name='product_detail'),
    # path('create_product/',views.create_product, name='create_product'),
    # path('create_product<std : pk>/',views.create_product, name='create_product'),
]