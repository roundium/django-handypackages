from django.contrib import admin

from .forms import BlogForm
from .models import Blog


class BlogAdminPanel(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'publish_time']
    filter_horizontal = ('tags', )
    fields = [
        'title', 'text', 'slug', 'image', 'tags', 'language', 'publish_time',
        'create_time',
    ]
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['create_time']
    form = BlogForm


admin.site.register(Blog, BlogAdminPanel)
