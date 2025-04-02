
from django.urls import path
from setuptools.extern import names

from . import views

app_name = 'orders'

urlpatterns= [
    path('cart/', views.CartView.as_view(), name='cart'),
    path('cat/add_item/<int:pk>', views.AddCartItemView.as_view(), name = 'add_cart_item'),
    path('cart/delete-item/<int:pk>/', views.DeleteCartItemView.as_view(), name = 'delete_cart_item'),
    path('cart/update-item/<int:pk>/', views.UpdateCartItemView.as_view(), name = 'Update_cart_item'),
    path('order/order_confirmation/', views.OrderConfirmationView.as_view(), name = 'order_confirmation'),
    path('order/add_order/', views.AddOrderView.as_view(), name='add_order'),
    path('orders/', views.ListOrderView.as_view(), name = 'orders'),
    path('orders/detail/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail')
]
