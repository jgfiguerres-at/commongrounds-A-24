from django.shortcuts import render

from .models import ProductType, Product


def item_list(request):
    items = Products.objects.all()

    return render(request, 'merchstore/item_list.html', {
        'items': items,
    })


def item_detail(request, id):
    item = Products.objects.get(pk=id)

    return render(request, 'merchstore/item_detail.html', {
        'recipe' : recipe,
        'ingredients': ingredients,
    })


class RecipeListView(ListView):
    model = Product
    template_name = 'merchstore/item_list.html' # default value


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'merchstore/item_detail.html' # default value
