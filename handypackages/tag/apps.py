from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TagConfig(AppConfig):
    name = 'handypackages.tag'
    verbose_name = _('Tag App')
