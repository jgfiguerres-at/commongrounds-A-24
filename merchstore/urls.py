from django.urls import path

from .views import *

urlpatterns = [
    path('merchstore/items', ItemListView.as_view(), name='item_list'),
    path('merchstore/item/<int:pk>', ItemDetailView.as_view(),
        name='item_detail'),
]

app_name = "merchstore"
