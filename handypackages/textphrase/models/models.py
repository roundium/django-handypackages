from django.db import models
from django.utils.translation import gettext_lazy as _


class TextPhraseAbstractModel(models.Model):
    """
    this is TextPhrase Abstract Model
    if you don't like fields or style of TextPhrase Model you can
    inheritance from this abstract model and overwrite it
    """
    title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_('Title')
    )
    phrase_type = models.CharField(
        db_index=True,
        max_length=255,
        verbose_name=_('Phrase Type')
    )
    text = models.TextField(
        verbose_name=_('Text')
    )
    language = models.CharField(
        default="global", max_length=6,
        verbose_name=_('Language')
    )

    def __str__(self):
        """
        return title by default.
        if title is null or empty phrase_type will be returned.
        """
        return self.title or self.phrase_type

    def __unicode__(self):
        return u'%s' % (self.title or self.phrase_type)

    class Meta:
        abstract = True
        ordering = ('phrase_type',)
        verbose_name = _('Text Phrase')
        verbose_name_plural = _('Text Phrases')


class TextPhrase(TextPhraseAbstractModel):
    """
    this model will implement TextPhraseAbstractModel.
    if you don't like style or fields you can import
    TextPhraseAbstractModel and overwrite this model,
    and then delete TextPhraseModel from settings.py.
    use this model for phrases that have text in it, not images
    like email, phone, location, copyright note, releated links,
    social network links, languages.
    text field length is limited to 2000 character
    you can add multiple text phrase with the same phrase type.
    example:
        title : phrase_type : text
        --------------------------
        copyright    : copyright    : 2018
        AboutUsFr    : aboutus      : AboutUs
        facebook url : facebook_url : https://facebook.com
    """
