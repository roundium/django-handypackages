from django.contrib import admin

from .forms import ProductForm
from .models import Product


class ProductAdminPanel(admin.ModelAdmin):
    form = ProductForm
    list_display = ['title', 'price', 'language', 'create_time']
    list_filter = ['language', 'create_time']
    filter_horizontal = ('tags', )
    fields = [
        'title',
        'text',
        'price',
        'slug',
        'image',
        'tags',
        'language',
        'create_time',
    ]
    search_fields = [
        'title',
        'price',
        'text',
        'language',
        'create_time',
        'tags__value',
    ]
    prepopulated_fields = {'slug': ('title', )}
    readonly_fields = ['create_time']


admin.site.register(Product, ProductAdminPanel)
