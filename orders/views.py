from pydoc import importfile
from venv import create

from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cart, CartItem

class CartView(LoginRequiredMixin, ListView):
    template_name = "cart/cart.html"
    context_object_name = 'cart_items'
    login_url = reverse_lazy('users:login')

    def get_queryset(self):
        cart, created =Cart.objects.get_or_create(user=self.request.user)
        return CartItem.objects.filter(cart=cart)


