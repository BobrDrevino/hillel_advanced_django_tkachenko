from django.urls import path

from products.views import ProductsView, ProductDetail, export_csv, ImportCSV

urlpatterns = [
    path('products', ProductsView.as_view(), name='products'),
    path('products/<uuid:pk>/', ProductDetail.as_view(),
         name='product_detail'),
    path('products/csv', export_csv, name='export_csv'),
    path('products/import_csv/', ImportCSV.as_view(), name='import_csv'),
]
