import tempfile

from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.utils import timezone
from filer.models import Image

from handypackages.blog.models import Blog, Tag


class TestBlogModels(TestCase):
    def setUp(self):
        # make temp folder because we want to delete files after test
        # and this code do that automatically
        settings.MEDIA_ROOT = tempfile.mkdtemp()

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

    def test_blog_model(self):
        self.assertEqual(
            str(self.blog),
            "blog test title",
            "__str__ in blog model have an issue!"
        )
        self.assertEqual(
            self.blog.__unicode__(),
            "blog test title",
            "__unicode__ in blog model have an issue!"
        )

        self.assertEqual(
            self.blog,
            Blog.published.all()[0],
            "published manager have an issue!"
        )

        self.assertEqual(
            set(Tag.objects.all()),
            set(self.blog.blog_tags),
            "blog blog_tags method does not work!"
        )

    def test_tag_model(self):
        self.assertEqual(
            str(self.tags[0]),
            "django",
            "Tag Model __str__ method have an issue!",
        )
        self.assertEqual(
            self.tags[0].__unicode__(),
            "django",
            "Tag Model __unicode__ method have an issue!",
        )
