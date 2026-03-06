from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Product


class ItemListView(ListView):
    model = Product
    template_name = 'merchstore/item_list.html' # default value


class ItemDetailView(DetailView):
    model = Product
    template_name = 'merchstore/item_detail.html' # default value
