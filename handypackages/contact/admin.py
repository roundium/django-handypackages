from django.contrib import admin

from .models import Contact


class ContactAdminPanel(admin.ModelAdmin):
    """ i disable add permission because of security issues """
    list_display = ['name', 'email', 'phone']
    search_fields = ['name', 'email', 'phone']
    readonly_fields = [
        'name',
        'email',
        'phone',
        'message',
        'time_send',
    ]
    list_filter = ['time_send']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Contact, ContactAdminPanel)
