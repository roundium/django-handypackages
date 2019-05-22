import tempfile

from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from filer.models import Image

from handypackages.tag.models import Tag

from .models import Gallery


class TestGalleryModels(TestCase):
    def setUp(self):
        # make temp folder because we want to delete files after test
        # and this code do that automatically
        settings.MEDIA_ROOT = tempfile.mkdtemp()

        self.user = User.objects.create_superuser('test_user', '', 'testing')

        self.tags = [
            Tag.objects.create(value='django'),
            Tag.objects.create(value='python'),
            Tag.objects.create(value='test'),
            Tag.objects.create(value='app'),
        ]

        with open('./handypackages/blog/tests/test_upload_image.jpg', 'rb') as image:
            test_image = SimpleUploadedFile(
                'test_upload_image.jpg',
                image.read(),
                content_type='image/jpeg'
            )
            image = Image(
                owner=self.user,
                file=test_image,
                original_filename='gallery_image_file',
                name='test_Gallery_image'
            )
            image.save()

        gallery = Gallery(
            title='gallery test title',
            text='gallery test',
            image=image,
        )
        gallery.save()
        gallery.tags.add(*self.tags)
        self.gallery = gallery

    def test_gallery_model(self):
        self.assertEqual(
            str(self.gallery),
            'gallery test title',
            '__str__ in gallery model have an issue!'
        )

        self.assertEqual(
            self.gallery.__unicode__(),
            'gallery test title',
            '__unicode__ in gallery model have an issue!'
        )

        self.assertEqual(
            set(Tag.objects.all()),
            set(self.gallery.gallery_tags),
            'gallery gallery_tags method does not work!'
        )
