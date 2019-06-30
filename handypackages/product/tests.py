import tempfile

from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from filer.models import Image

from handypackages.tag.models import Tag

from .models import Product


class TestProductModels(TestCase):
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

        with open('./handypackages/test_requirements/test_upload_image.jpg',
                  'rb') as image:
            test_image = SimpleUploadedFile(
                'test_upload_image.jpg',
                image.read(),
                content_type='image/jpeg'
            )
            image = Image(
                owner=self.user,
                file=test_image,
                original_filename='product_image_file',
                name='test_product_image'
            )
            image.save()

        product = Product(
            title='product test title',
            text='product test',
            slug='product-test-title',
            image=image,
            price="25000 T"
        )
        product.save()
        product.tags.add(*self.tags)
        self.product = product

    def test_product_model(self):
        self.assertEqual(
            str(self.product),
            'product test title',
            '__str__ in product model have an issue!'
        )

        self.assertEqual(
            self.product.__unicode__(),
            'product test title',
            '__unicode__ in product model have an issue!'
        )

        self.assertEqual(
            set(Tag.objects.all()),
            set(self.product.product_tags),
            'blog blog_tags method does not work!'
        )
