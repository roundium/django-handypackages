from django.test import RequestFactory, TestCase, override_settings
from django.urls import reverse

from handypackages.textphrase.models import TextPhrase
from handypackages.settings import (TEXT_PHRASE_LANG_CONTEXT_OBJECT_NAME,
                                 TEXT_PHRASE_SIMPLE_CONTEXT_OBJECT_NAME,)


class ContextProcessorsTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        # create some records for testing
        self.first_phrase = TextPhrase.objects.create(
            phrase_type="language", text="welcome", language="en")
        self.first_phrase = TextPhrase.objects.create(
            phrase_type="language", text="Bienvenue", language="fr")
        self.second_phrase = TextPhrase.objects.create(
            phrase_type="facebook_page", text="https://facebook.com",
            language="global")

        self.all_phrases = TextPhrase.objects.all()

    def test_simple_text_phrase_cp(self):
        response = self.client.get(reverse("admin:index"), follow=True)
        self.assertEqual(
            set(response.context[TEXT_PHRASE_SIMPLE_CONTEXT_OBJECT_NAME]),
            set(self.all_phrases),
            "text_phrase_simple_cp context processor does not work")

    @override_settings(LANGUAGE_CODE='fr', LANGUAGES=(('fr', 'French'),))
    def test_lang_text_phrase(self):
        response = self.client.get(reverse("admin:index"), follow=True)
        self.assertEqual(
            set(response.context[TEXT_PHRASE_LANG_CONTEXT_OBJECT_NAME]),
            set(TextPhrase.objects.filter(language="fr")),
            "text_phrase_language_cp context processor does not work")
