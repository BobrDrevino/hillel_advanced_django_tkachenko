from django.views.generic import ListView, DetailView

from products.models import Product


class ProductsView(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product