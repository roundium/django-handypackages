from django.template import Context, Template
from django.test import TestCase

from handypackages.textphrase.models import TextPhrase


class TemplateTagsTests(TestCase):
    def setUp(self):
        TextPhrase.objects.create(
            phrase_type="language", text="welcome", language="en")
        TextPhrase.objects.create(
            phrase_type="language", text="bienvenu", language="fr")
        TextPhrase.objects.create(
            phrase_type="language", text="Bonjour", language="fr")
        TextPhrase.objects.create(
            phrase_type="facebook_page", text="https://facebook.com",
            language="global")

    def render_template(self, string, context=None):
        context = context or {}
        context = Context(context)
        return Template(string).render(context)

    def test_text_phrases_tags(self):
        self.assertRaises(
            Exception,
            self.render_template,
            string='{% load phrases_tags %}'
            '{% single_text_phrase "facebook_page" as facebook_page %}'
            '<a href="{{ facebook_page }}">Facebook Page<a/>'
        )

        phrases = TextPhrase.objects.all()
        rendered = self.render_template(
            '{% load phrases_tags %}'
            '{% single_text_phrase "facebook_page" as facebook_page %}'
            '<a href="{{ facebook_page.text }}">Facebook Page<a/>',
            {'text_phrases': phrases}
        )
        answer = '<a href="https://facebook.com">Facebook Page<a/>'
        self.assertEqual(rendered, answer,
                         "single_text_phrase templatetag does not work")

        rendered = self.render_template(
            '{% load phrases_tags %}'
            '{% single_text_phrase "language" "en" as lang %}'
            '<p>{{ lang.text }}</p>',
            {'text_phrases': phrases}
        )
        answer = '<p>welcome</p>'
        self.assertEqual(rendered, answer,
                         "single_text_phrase templatetag does not work")

        rendered = self.render_template(
            '{% load phrases_tags %}'
            '{% multi_text_phrase "language" as languages %}'
            '{% for lang in languages %}'
            '<p>{{ lang.text }}</p>'
            '{% endfor %}',
            {'text_phrases': phrases}
        )
        answer = ('<p>welcome</p>'
                  '<p>bienvenu</p>'
                  '<p>Bonjour</p>')
        self.assertEqual(rendered, answer,
                         "multi_text_phrase templatetag does not work")

        rendered = self.render_template(
            '{% load phrases_tags %}'
            '{% multi_text_phrase "language" "fr" as languages %}'
            '{% for lang in languages %}'
            '<p>{{ lang.text }}</p>'
            '{% endfor %}',
            {'text_phrases': phrases}
        )
        answer = ('<p>bienvenu</p>'
                  '<p>Bonjour</p>')
        self.assertEqual(rendered, answer,
                         "multi_text_phrase templatetag does not work")

        self.assertRaises(
            Exception,
            self.render_template,
            string='{% load phrases_tags %}'
            '{% multi_text_phrase "language" "fr" as languages %}'
            '{% for lang in languages %}'
            '<p>{{ lang.text }}</p>'
            '{% endfor %}'
        )
