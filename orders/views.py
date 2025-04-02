from itertools import product
from lib2to3.fixes.fix_input import context
from pydoc import importfile
from urllib.response import addbase
from venv import create

from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, View, DeleteView, FormView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from sympy.stats import quantile

from .models import Cart, CartItem, Address, Order, OrderItem
from shop.models import Products
from django.contrib import messages
from .forms import AddressForm

class CartView(LoginRequiredMixin, ListView):
    template_name = "cart/cart.html"
    context_object_name = 'cart_items'
    login_url = reverse_lazy('users:login')

    def get_queryset(self):
        cart, created =Cart.objects.get_or_create(user=self.request.user)
        return CartItem.objects.filter(cart=cart)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_items = self.get_queryset()
        total_amount = sum( item.product.price * item.quantity for item in cart_items)
        context['total_amount'] = total_amount
        return context


class AddCartItemView(LoginRequiredMixin, View):
    def get(self, request, pk):
        add_to_cart = True
        product = get_object_or_404(Products, pk=pk)

        try:
            cart, _ = Cart.objects.get_or_create(user=request.user)
            if product.stock > 0:
                cart_item, cart_item_created = CartItem.objects.get_or_create(cart=cart, product=product)

                if not cart_item_created:
                    cart_item.quantity += 1
                elif cart_item.created:
                    cart_item.quantity = 1

                cart_item.save()
            else:
                add_to_cart = False
        except Exception as ex:
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            if add_to_cart:
                messages.success(request, f'{product.name} added to Cart')
            else:
                messages.error(request, f'{product.name} Out of Stock')

            return redirect(request.META.get('HTTP_REFERER'))

class DeleteCartItemView(LoginRequiredMixin, DeleteView):
    model = CartItem
    success_url = reverse_lazy('orders:cart')

class UpdateCartItemView(View):
    def post(self, request, pk):
        cart_item = CartItem.objects.get(pk=pk, cart__user = request.user)
        new_quantity = int(request.POST.get('quantity'))
        if 0 < new_quantity <= cart_item.product.stock:
            cart_item.quantity = new_quantity
            cart_item.save()
        return redirect('orders:cart')

class OrderConfirmationView(LoginRequiredMixin, ListView, FormView ):
    login_url = reverse_lazy('users:login')
    template_name = 'orders/order_confirmation.html'
    form_class = AddressForm
    context_object_name = 'cart_items'
    success_url = reverse_lazy('orders:add_order')

    def get_queryset(self):
        cart = Cart.objects.get(user = self.request.user)
        return CartItem.objects.filter(cart=cart)

    def form_valid(self, form):
        address = form.save()
        self.request.session['address_id'] = address.id
        return redirect(self.get_success_url())
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_items  = self.get_queryset()

        if self.request.method == 'GET':
            context['form'] = self.form_class()
        total_amount = sum(item.product.price * item.quantity for item in cart_items)
        context['total_amount'] = total_amount
        return context

class AddOrderView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')
    def get(self, request):
        user = request.user
        cart = get_object_or_404(Cart, user=user)
        cart_items = CartItem.objects.filter(cart=cart)
        if not cart_items:
            return redirect('orders:cart')

        address_id = request.session.get('address_id')
        if not address_id:
            return redirect('orders:order_confirmation')
        address = get_object_or_404(Address, id = address_id)
        order = Order.objects.create(user = user, order_address = address, total_amount = 0 )
        total_amount = 0
        for item in cart_items:
            OrderItem.objects.create(order=order, product=item.product, quantity = item.quantity)
            total_amount += item.product.price * item.quantity

            product = item.product
            product.stock -= item.quantity
            product.save()
            item.delete()
        order.total_amount = total_amount
        order.save()
        del request.session['address_id']
        return redirect('orders:cart')

class ListOrderView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users:login')
    model = Order
    template_name = 'orders/orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')

class OrderDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('users:login')
    model = Order
    template_name = 'orders/order_detail.html'
    context_object_name = 'order'

    def get_queryset(self):
        return Order.objects.filter(user = self.request.user)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_items'] = OrderItem.objects.filter(order=self.object)
        return context