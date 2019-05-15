from django.contrib import admin

from .forms import TextPhraseForm
from .models import TextPhrase


class TextPhraseAdminPanel(admin.ModelAdmin):
    list_display = ['title', 'phrase_type', 'text']
    search_fields = ['title', 'phrase_type', 'text']
    form = TextPhraseForm


admin.site.register(TextPhrase, TextPhraseAdminPanel)
