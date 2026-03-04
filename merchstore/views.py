from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import ProductType, Product


def item_list(request):
    items = Product.objects.all()

    return render(request, 'merchstore/item_list.html', {
        'items': items,
    })


def item_detail(request, id):
    item = Product.objects.get(pk=id)

    return render(request, 'merchstore/item_detail.html', {
        'item': item,
    })


class ItemListView(ListView):
    model = Product
    template_name = 'merchstore/item_list.html' # default value


class ItemDetailView(DetailView):
    model = Product
    template_name = 'merchstore/item_detail.html' # default value
