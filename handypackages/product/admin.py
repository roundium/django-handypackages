from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from handypackages.datetime_conv import fmt

from .forms import ProductForm
from .models import Product


class ProductAdminPanel(admin.ModelAdmin):
    def convert_create_time_to_persian(self, obj):
        if obj.language == 'fa':
            return fmt(obj.create_time, "%d %n %y ساعت %h:%M")
        return str(obj.create_time)
    convert_create_time_to_persian.short_description = _('Time Create')

    form = ProductForm
    list_display = [
        'title', 'price', 'language', 'convert_create_time_to_persian',
    ]
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
