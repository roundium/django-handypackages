from django.db import models
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class ContactAbstractModel(models.Model):
    """
    if you don't like contact model
    inherite from this abstract models and overwrite it
    """
    name = models.CharField(verbose_name=_("Name"), max_length=255)
    email = models.EmailField(verbose_name=_("Email"), max_length=255)
    phone = PhoneNumberField(verbose_name=_("Phone"), null=False, blank=False)
    message = models.TextField(verbose_name=_("Message"))
    time_send = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Time Send'))

    def __str__(self):
        return self.email

    def __unicode__(self):
        return u'%s' % self.email

    class Meta:
        abstract = True
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')


class Contact(ContactAbstractModel):
    """ Contact Model """
