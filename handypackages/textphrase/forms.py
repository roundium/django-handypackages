from django import forms
from easy_select2.widgets import Select2

from handypackages.settings import TEXT_PHRASE_LANGUAGES

from .models import TextPhrase


class TextPhraseForm(forms.ModelForm):
    language = forms.ChoiceField(
        choices=TEXT_PHRASE_LANGUAGES(), widget=Select2())

    class Meta:
        model = TextPhrase
        fields = '__all__'
