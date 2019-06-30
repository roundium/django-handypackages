from django.test import TestCase

from .models import Tag


class TagModelTest(TestCase):
    def setUp(self):
        self.tags = [
            Tag.objects.create(value='django'),
            Tag.objects.create(value='python'),
            Tag.objects.create(value='test'),
            Tag.objects.create(value='app'),
        ]

    def test_tag_model(self):
        self.assertEqual(
            str(self.tags[0]),
            'django',
            'Tag Model __str__ method have an issue!',
        )
        self.assertEqual(
            self.tags[0].__unicode__(),
            'django',
            'Tag Model __unicode__ method have an issue!',
        )
