from django.urls import path, include

from .views import HomeView, ItemDetailView, add_to_cart, checkout

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', checkout, name='checkout'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', add_to_cart, name='remove-from-cart'),
    path(r'^accounts/', include('allauth.urls'))
]
