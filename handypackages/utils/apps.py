from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PackageUtilsConfig(AppConfig):
    name = 'handypackages.utils'
    verbose_name = _('Utils App')
