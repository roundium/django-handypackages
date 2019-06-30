from django.contrib import admin

from .models import Subscribe


class SubscribeAdminPanel(admin.ModelAdmin):
    list_display = ['email', 'create_time']
    list_filter = ['create_time']
    search_fields = ['email']
    readonly_fields = ['create_time']


admin.site.register(Subscribe, SubscribeAdminPanel)
