from django.test import TestCase

from handypackages.textphrase.models import TextPhrase


class TextPhraseModelTests(TestCase):
    def setUp(self):
        self.first_phrase = TextPhrase.objects.create(
            phrase_type="language", text="welcome", language="en")
        self.second_phrase = TextPhrase.objects.create(
            phrase_type="facebook_page", text="https://facebook.com",
            language="global")

    def test_text_phrase_model_methods(self):
        self.assertEqual(str(self.first_phrase), "language",
                         "__str__ Of TextPhrase Model Have Issue!")
        self.assertEqual(self.first_phrase.__unicode__(), "language",
                         "__unicode__ Of TextPhrase Model Have Issue!")
