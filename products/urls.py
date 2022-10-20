from django.urls import path

from products.views import ProductsView, ProductDetail

urlpatterns = [
    path('products', ProductsView.as_view(), name='products'),
    path('products/<uuid:pk>/', ProductDetail.as_view(),
         name='product_detail'),
]
