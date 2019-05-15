from django import forms
from easy_select2.widgets import Select2

from handypackages.settings import (TEXT_PHRASE_LANGUAGES,
                                 TEXT_PHRASE_MODEL_PHRASE_TYPES,)
from handypackages.textphrase.models import TextPhrase


class TextPhraseForm(forms.ModelForm):
    phrase_type = forms.ChoiceField(
        choices=TEXT_PHRASE_MODEL_PHRASE_TYPES, widget=Select2())
    language = forms.ChoiceField(
        choices=TEXT_PHRASE_LANGUAGES(), widget=Select2())

    class Meta:
        model = TextPhrase
        fields = '__all__'
