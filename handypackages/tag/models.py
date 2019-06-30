from django.db import models
from django.utils.translation import gettext_lazy as _


class TagAbstractMode(models.Model):
    value = models.CharField(
        verbose_name=_('Value'),
        max_length=255,
        unique=True,
        db_index=True
    )
    create_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Time of Create')
    )

    def __str__(self):
        return self.value

    def __unicode__(self):
        return u'%s' % self.value

    class Meta:
        abstract = True
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class TagModel(TagAbstractMode):
    """ Tags will use with product app """


class Tag(TagModel):
    class Meta:
        proxy = True
        app_label = 'handypackages'
        auto_created = True
