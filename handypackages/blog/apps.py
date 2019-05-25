from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class BlogConfig(AppConfig):
    name = 'handypackages.blog'
    verbose_name = _('Blog App')
