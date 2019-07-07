from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.db.models.manager import Manager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField

from handypackages.tag.models import TagModel


class PublishedBlogManager(Manager):
    def get_queryset(self):
        return super(PublishedBlogManager,
                     self).get_queryset().filter(
            publish_time__lte=timezone.now(),
            disable=False
        )


class BlogAbstractModel(models.Model):
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
    create_time = models.DateTimeField(
        verbose_name=_('Time Create'),
        editable=False,
        auto_now_add=True
    )
    publish_time = models.DateTimeField(
        verbose_name=_('Publish Time'),
        auto_now=False,
        auto_now_add=False
    )
    slug = models.SlugField(
        unique=True,
        allow_unicode=True,
        max_length=255,
        verbose_name=_('Slug')
    )
    tags = models.ManyToManyField(TagModel, blank=True)
    language = models.CharField(
        default="global",
        max_length=6,
        db_index=True,
        verbose_name=_('Language'),
    )
    disable = models.BooleanField(
        default=False,
        verbose_name=_('Disable'),
        help_text=_('Prevent blog showing immediately')
    )

    # default django manager
    objects = models.Manager()

    # published manager will return published news
    published = PublishedBlogManager()

    def __str__(self):
        """ will return the blog title """
        return self.title

    def __unicode__(self):
        return u'%s' % self.title

    @property
    def blog_tags(self):
        """ will return all blog tags """
        return self.tags.all()

    class Meta:
        abstract = True
        ordering = ('-publish_time',)
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')


class BlogModel(BlogAbstractModel):
    """Blog model."""


class Blog(BlogModel):
    class Meta:
        proxy = True
        app_label = 'handypackages'
        auto_created = True
        ordering = ('-publish_time', )
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')
