from django.contrib import admin

from .models import Blog, Tag


class BlogAdminPanel(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'publish_time']
    filter_horizontal = ('tags', )
    fields = ['title', 'text', 'slug', 'image',
              'tags', 'publish_time', 'create_time']
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ['create_time']


class TagAdminPanel(admin.ModelAdmin):
    list_display = ['value', 'create_time']
    readonly_fields = ['create_time']


admin.site.register(Blog, BlogAdminPanel)
admin.site.register(Tag, TagAdminPanel)
