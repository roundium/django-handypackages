from django import forms
from easy_select2.widgets import Select2

from handypackages.settings import ALL_LANGUAGES

from .models import Product


class ProductForm(forms.ModelForm):
    language = forms.ChoiceField(
        choices=ALL_LANGUAGES, widget=Select2())

    class Meta:
        model = Product
        fields = '__all__'
