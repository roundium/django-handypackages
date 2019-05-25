from django.contrib import admin

from .models import Gallery


class GalleryAdminPanel(admin.ModelAdmin):
    list_display = ['title', 'create_time']
    list_filter = ['create_time']
    filter_horizontal = ('tags', )
    fields = ['title', 'text', 'image', 'tags', 'create_time']
    readonly_fields = ['create_time']


admin.site.register(Gallery, GalleryAdminPanel)
