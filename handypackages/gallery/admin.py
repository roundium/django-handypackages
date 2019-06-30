from django.contrib import admin

from .forms import GalleryForm
from .models import Gallery


class GalleryAdminPanel(admin.ModelAdmin):
    list_display = ['title', 'create_time']
    list_filter = ['create_time']
    filter_horizontal = ('tags', )
    fields = ['title', 'text', 'image', 'language', 'tags', 'create_time']
    readonly_fields = ['create_time']
    form = GalleryForm


admin.site.register(Gallery, GalleryAdminPanel)
