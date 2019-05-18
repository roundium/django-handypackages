from django.contrib import admin

from .forms import TextPhraseForm
from .models import TextPhrase


class TextPhraseAdminPanel(admin.ModelAdmin):
    list_display = ['title', 'slug', 'text']
    search_fields = ['title', 'slug', 'text']
    prepopulated_fields = {'slug': ('title',), }
    form = TextPhraseForm


admin.site.register(TextPhrase, TextPhraseAdminPanel)
