from django.views.generic import TemplateView


class ProductsView(TemplateView):
    template_name = 'products/index.html'