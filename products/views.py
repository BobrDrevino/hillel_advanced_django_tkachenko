import csv

from django.conf import settings
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from products.models import Product


class ProductsView(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product


def export_csv(request, *args, **kwargs):
    response = HttpResponse(
        content_type='text/csv',
        headers={
            'Content-Disposition': 'attachment; filename="products.csv"'
        }
    )
    fieldnames = ['name', 'description', 'price', 'sku', 'category', 'image']
    writer = csv.DictWriter(response, fieldnames=fieldnames)
    writer.writeheader()

    for product in Product.objects.iterator():
         writer.writerow(
             {'name': product.name,
              'description': product.description,
              'price': product.price,
              'sku': product.sku,
              'category': product.category,
              'image': settings.DOMAIN + product.image.url
              }
         )

    return response
