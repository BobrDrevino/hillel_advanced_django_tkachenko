from django.contrib import admin
from django.utils.safestring import mark_safe

from products.models import Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    filter_horizontal = ('products',)
    list_display = ('name', 'price', 'sku', 'created_at')
    list_filter = ('price', )
    readonly_fields = ('id',)

    def product_image(self, obj):
        if obj.image:
            return mark_safe((
                '<img src="{}" width="64" height="64" />'.format(
                    obj.image.url)))
        return ''


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_image', 'name',)

    def category_image(self, obj):
        if obj.image:
            return mark_safe((
                '<img src="{}" width="64" height="64" />'.format(obj.image.url))) # noqa
        return ''
