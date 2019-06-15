from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField

from handypackages.tag.models import TagModel


class ProductAbstractModel(models.Model):
    """
    Product Abstract class.
    if you don't like product model inherite this model and overwrite it
    """
    title = models.CharField(
        max_length=255,
        verbose_name=_('Title')
    )
    image = FilerImageField(
        verbose_name=_('Image'),
        on_delete=models.CASCADE
    )
    text = RichTextUploadingField(
        verbose_name=_('Text')
    )

    price = models.CharField(
        max_length=255,
        help_text=_('235,000 T'),
        verbose_name=_('Price')
    )
    slug = models.SlugField(
        unique=True,
        allow_unicode=True,
        max_length=255,
        verbose_name=_('Slug')
    )
    tags = models.ManyToManyField(TagModel, blank=True)

    create_time = models.DateTimeField(
        verbose_name=_('Time Create'),
        editable=False,
        auto_now_add=True
    )

    def __str__(self):
        return self.title

    def __unicode__(self):
        return u'%s' % self.title

    @property
    def product_tags(self):
        """ will return all product tags """
        return self.tags.all()

    class Meta:
        abstract = True
        ordering = ('-create_time',)
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class ProductModel(ProductAbstractModel):
    """
    Product Model
    if you don't like product model
    inherite ProductAbstractModel model and overwrite it
    """


class Product(ProductModel):
    class Meta:
        proxy = True
        app_label = 'handypackages'
        auto_created = True
