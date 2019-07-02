from django.contrib import admin

from .forms import BlogForm
from .models import Blog


class BlogAdminPanel(admin.ModelAdmin):
    list_display = [
        'title',
        'language',
        'create_time',
        'publish_time',
        'disable',
    ]
    filter_horizontal = ('tags', )
    fields = [
        'title',
        'text',
        'slug',
        'image',
        'tags',
        'language',
        'publish_time',
        'create_time',
        'disable',
    ]
    list_filter = ['language', 'disable', 'create_time', 'publish_time']
    search_fields = [
        'title',
        'create_time',
        'text',
        'language',
        'tags__value',
    ]
    prepopulated_fields = {'slug': ('title', )}
    readonly_fields = ['create_time']
    form = BlogForm


admin.site.register(Blog, BlogAdminPanel)
