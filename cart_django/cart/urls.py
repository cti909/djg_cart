from django.urls import path
from . import views

urlpatterns = [
    path('cart_home',views.cart_home, name='cart_home'),
    path('cart_add/', views.cart_add, name='add_cart'),
    # path('cart_add/', views.cart_addp, name='cart_add'),
    path('cart_edit/<int:id>', views.cart_edit, name='cart_edit'),
    path('cart_delete/<int:id>', views.cart_delete, name='cart_delete'),
    path('history_home/',views.history_home, name='history_home'),
    path('payment/',views.payment, name='payment'),
    path('order_view/',views.order_view, name='order_view'),
    path('cart_edit/<int:id>/<int:number>', views.cart_edit, name='cart_edit'),
]   
