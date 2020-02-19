from django.urls import include, path

from .views import (HomeView, ItemDetailView, OrderSummaryView, add_to_cart,
                    checkout, remove_from_cart, remove_single_item_from_cart)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', checkout, name='checkout'),
    path('cart/', OrderSummaryView.as_view(), name='cart'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path(
        'remove-from-cart/<slug>/',
        remove_from_cart,
        name='remove-from-cart',
    ),
    path(
        'remove-single-item-from-cart/<slug>/',
        remove_single_item_from_cart,
        name='remove-single-item-from-cart',
    ),
    path('accounts/', include('allauth.urls'))
]
