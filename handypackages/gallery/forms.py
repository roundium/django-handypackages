from django import forms
from django.utils.translation import gettext_lazy as _
from easy_select2.widgets import Select2

from handypackages.settings import ALL_LANGUAGES

from .models import Gallery


class GalleryForm(forms.ModelForm):
    language = forms.ChoiceField(
        choices=ALL_LANGUAGES,
        widget=Select2(),
        label=_('Language'),
    )

    class Meta:
        model = Gallery
        fields = '__all__'
