from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .forms import *
from .models import *


class ProductListView(ListView):
    model = Product
    template_name = 'merchstore/item_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            profile = self.request.user.profile
            owned = Product.objects.filter(owner=profile)
            other = Product.objects.exclude(owner=profile)

            context['owned_products'] = owned
            context['all_products'] = other
        else:
            context['all_products'] = Product.objects.all()

        return context


class ProductDetailView(DetailView, CreateView):
    model = Product
    form_class = TransactionForm
    template_name = 'merchstore/item_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        has_stock = product.stock >= 1

        is_owner = False
        if self.request.user.is_authenticated:
            profile = self.request.user.profile
            is_owner = (product.owner == profile)

        context['is_owner'] = is_owner
        context['has_stock'] = has_stock
        context['product'] = product

        return context

    def get_success_url(self):
        return reverse_lazy('merchstore:cart')

    def form_valid(self, form):
        product = self.get_object()
        amount = form.cleaned_data.get('amount')

        if product.stock < amount:
            return self.form_invalid(form)

        if product.stock == 0:
            product.status = 'Out of Stock'

        form.instance.buyer = self.request.user.profile
        form.instance.product = self.get_object()
        form.instance.amount = amount

        product.stock -= amount
        product.save()

        return super().form_valid(form)


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    template_name = 'merchstore/item_add.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        if not request.user.groups.filter(name='Market Seller').exists():
            return redirect('merchstore:item_list')

        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)


class ProductUpdateView(UpdateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    template_name = 'merchstore/item_update.html'

    def get(self, request, *args, **kwargs):
        profile = self.request.user.profile
        product = self.get_object()

        if not request.user.is_authenticated:
            return redirect('login')

        if not request.user.groups.filter(name='Market Seller').exists():
            return redirect('merchstore:item_list')

        if not product.owner == profile:
            return redirect('merchstore:item_detail', pk=product.pk)

        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        profile = self.request.user.profile
        product = self.get_object()

        if not self.request.user.groups.filter(name='Market Seller').exists():
            return redirect('merchstore:item_list')

        if not product.owner == profile:
            return redirect('merchstore:item_detail', pk=product.pk)

        if self.object.stock == 0:
            self.object.status = "Out of Stock"

        self.object.save()

        return super().form_valid(form)


class CartView(ListView, LoginRequiredMixin):
    model = Transaction
    template_name = 'merchstore/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            profile = self.request.user.profile
            purchased = Transaction.objects.filter(buyer=profile)
            owners = []
            for transaction in purchased:
                if transaction.product.owner not in owners:
                    owners.append(transaction.product.owner)

            context['purchased_products'] = purchased
            context['product_owners'] = owners

        return context


class TransactionListView(ListView, LoginRequiredMixin):
    model = Transaction
    template_name = 'merchstore/transaction_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            profile = self.request.user.profile
            owned = Transaction.objects.filter(product__owner=profile)
            buyers = []
            for transaction in owned:
                if transaction.buyer not in buyers:
                    buyers.append(transaction.buyer)

            context['owned_products'] = owned
            context['product_buyers'] = buyers

        return context
