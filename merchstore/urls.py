from django.urls import path

from .views import *

urlpatterns = [
    path('items', ProductListView.as_view(), name='item_list'),
    path('item/<int:pk>', ProductDetailView.as_view(),
         name='item_detail'),
    path('item/add', ProductCreateView.as_view(),
         name='item_create'),
    path('item/<int:pk>/edit', ProductUpdateView.as_view(),
         name='item_update'),
    path('cart', CartView.as_view(), name='cart'),
    path('transactions', TransactionListView.as_view(),
         name='transaction_list'),
]

app_name = "merchstore"
