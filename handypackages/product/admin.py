from django.contrib import admin

from .forms import ProductForm
from .models import Product


class ProductAdminPanel(admin.ModelAdmin):
    form = ProductForm
    list_display = ['title', 'price', 'create_time']
    filter_horizontal = ('tags', )
    fields = ['title', 'text', 'price', 'slug', 'image',
              'tags', 'language', 'create_time']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['create_time']


admin.site.register(Product, ProductAdminPanel)
