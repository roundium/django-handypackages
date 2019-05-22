import tempfile

from django.conf import settings
from django.conf.urls import url
from django.contrib.auth.models import User
from django.contrib.sitemaps.views import sitemap
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import RequestFactory, TestCase
from django.urls import reverse_lazy
from django.utils import timezone
from filer.models import Image

from handypackages.blog.models import Blog, Tag
from handypackages.blog.rss_feed.example_urls import urlpatterns
from handypackages.blog.rss_feed.view import BlogFeed


def simple_blog_single_view(request, slug):
    pass


class TestRssFeedView(TestCase):
    def setUp(self):
        # make temp folder because we want to delete files after test
        # and this code do that automatically
        settings.MEDIA_ROOT = tempfile.mkdtemp()

        urlpatterns.append(
            url(r"^blog/(?P<slug>[\w-]+)/$", simple_blog_single_view,
                name="blog-single"),
        )

        self.factory = RequestFactory()

        self.user = User.objects.create_superuser("test_user", "", "testing")

        self.tags = [
            Tag.objects.create(value="django"),
            Tag.objects.create(value="python"),
            Tag.objects.create(value="test"),
            Tag.objects.create(value="app"),
        ]

        with open("./handypackages/blog/tests/test_upload_image.jpg", 'rb') as image:
            test_image = SimpleUploadedFile(
                "test_upload_image.jpg",
                image.read(),
                content_type="image/jpeg"
            )
            image = Image(
                owner=self.user,
                file=test_image,
                original_filename="blog_image_file",
                name='test_blog_image'
            )
            image.save()

        blog = Blog(
            title='blog test title',
            text='blog test',
            slug='blog-test-title',
            image=image,
            publish_time=timezone.now()
        )
        blog.save()
        blog.tags.add(*self.tags)
        self.blog = blog

    def test_default_rss_feed(self):
        request = self.factory.get('/blog/rss/')

        request.user = self.user

        self.assertRaises(
            Exception,
            BlogFeed,
            limit=50,
            link=reverse_lazy("blog-feed-default"),
            title="Blog Site Title",
            description="Site Blog Feed"
        )

        response = BlogFeed(
            limit=50,
            url_name="blog-single",
            link=reverse_lazy("blog-feed-default"),
            title="Blog Site Title",
            description="Site Blog Feed"
        )
        response.__call__(request)

    def test_atom_rss_feed(self):
        request = self.factory.get('/blog/rss/')

        request.user = self.user

        response = BlogFeed(
            limit=50,
            url_name="blog-single",
            link=reverse_lazy("blog-feed-atom"),
            title="Blog Site Title",
            description="Site Blog Feed",
            feed_type="atom"
        )
        response.__call__(request)
