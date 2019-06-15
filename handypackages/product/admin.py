from django.contrib import admin
from easy_select2 import select2_modelform

from .models import Product


class ProductAdminPanel(admin.ModelAdmin):
    form = select2_modelform(Product, attrs={'width': '300px'})
    list_display = ['title', 'price', 'create_time']
    filter_horizontal = ('tags', )
    fields = ['title', 'text', 'price', 'slug', 'image',
              'tags', 'create_time']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['create_time']


admin.site.register(Product, ProductAdminPanel)
