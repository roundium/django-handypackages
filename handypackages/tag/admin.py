from django.contrib import admin

from .models import Tag


class TagAdminPanel(admin.ModelAdmin):
    list_display = ['value', 'create_time']
    search_fields = ['value', 'create_time']
    list_filter = ['create_time']
    readonly_fields = ['create_time']


admin.site.register(Tag, TagAdminPanel)
