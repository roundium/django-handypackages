from django.contrib import admin

from .forms import TextPhraseForm
from .models import TextPhrase


class TextPhraseAdminPanel(admin.ModelAdmin):
    list_display = ['title', 'slug', 'text', 'language']
    search_fields = ['title', 'slug', 'text', 'language']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['language']
    form = TextPhraseForm


admin.site.register(TextPhrase, TextPhraseAdminPanel)
