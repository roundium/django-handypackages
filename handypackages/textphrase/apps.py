from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TextPhraseConfig(AppConfig):
    name = 'handypackages.textphrase'
    verbose_name = _('Text Phrase App')
