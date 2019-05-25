from django.test import TestCase

from handypackages.textphrase.models import TextPhrase


class TextPhraseModelTests(TestCase):
    def setUp(self):
        self.first_phrase = TextPhrase.objects.create(
            slug='language', text='welcome', language='en')

    def tearDown(self):
        TextPhrase.objects.all().delete()

    def test_text_phrase_model_methods(self):
        self.assertEqual(str(self.first_phrase), 'language',
                         '__str__ Of TextPhrase Model Have Issue!')
        self.assertEqual(self.first_phrase.__unicode__(), 'language',
                         '__unicode__ Of TextPhrase Model Have Issue!')
