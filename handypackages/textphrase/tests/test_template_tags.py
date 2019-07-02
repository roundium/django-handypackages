from django.template import Context, Template
from django.test import TestCase

from handypackages.textphrase.models import TextPhrase


class TemplateTagsTests(TestCase):
    def setUp(self):
        TextPhrase.objects.create(
            slug='language', text='welcome', language='en')
        TextPhrase.objects.create(
            slug='language', text='bienvenu', language='fr')
        TextPhrase.objects.create(
            slug='language', text='salut', language='fr')
        TextPhrase.objects.create(
            slug='facebook_page', text='https://facebook.com',
            language='global')

    def tearDown(self):
        TextPhrase.objects.all().delete()

    def render_template(self, string, context=None):
        context = context or {}
        context = Context(context)
        return Template(string).render(context)

    def test_text_phrases_tags(self):
        phrases = TextPhrase.objects.none()
        rendered = self.render_template(
            '{% load phrases_tags %}'
            '{% single_text_phrase "facebook_page" as facebook_page %}'
            '<a href="{{ facebook_page.text }}">Facebook Page<a/>',
            {'text_phrases': phrases}
        )
        answer = '<a href="">Facebook Page<a/>'
        self.assertEqual(rendered, answer,
                         'single_text_phrase templatetag does not work')

        phrases = TextPhrase.objects.all()
        rendered = self.render_template(
            '{% load phrases_tags %}'
            '{% single_text_phrase "facebook_page" as facebook_page %}'
            '<a href="{{ facebook_page.text }}">Facebook Page<a/>',
            {'text_phrases': phrases}
        )
        answer = '<a href="https://facebook.com">Facebook Page<a/>'
        self.assertEqual(rendered, answer,
                         'single_text_phrase templatetag does not work')

        rendered = self.render_template(
            '{% load phrases_tags %}'
            '{% single_text_phrase "language" "en" as lang %}'
            '<p>{{ lang.text }}</p>',
            {'text_phrases': phrases}
        )
        answer = '<p>welcome</p>'
        self.assertEqual(rendered, answer,
                         'single_text_phrase templatetag does not work')

        rendered = self.render_template(
            '{% load phrases_tags %}'
            '{% multi_text_phrase "language" as languages %}'
            '{% for lang in languages %}'
            '<p>{{ lang.text }}</p>'
            '{% endfor %}',
            {'text_phrases': phrases}
        )
        answer = ""
        text_phrases = TextPhrase.objects.filter(slug='language')
        for phrase in text_phrases:
            answer = answer + "<p>%s</p>" % phrase.text
        self.assertEqual(rendered, answer,
                         'multi_text_phrase templatetag does not work')

        rendered = self.render_template(
            '{% load phrases_tags %}'
            '{% multi_text_phrase "language" "fr" as languages %}'
            '{% for lang in languages %}'
            '<p>{{ lang.text }}</p>'
            '{% endfor %}',
            {'text_phrases': phrases}
        )
        answer = ('<p>salut</p><p>bienvenu</p>')
        self.assertEqual(rendered, answer,
                         'multi_text_phrase templatetag does not work')

        phrases = TextPhrase.objects.none()
        rendered = self.render_template(
            '{% load phrases_tags %}'
            '{% multi_text_phrase "language" "fr" as languages %}'
            '{% for lang in languages %}'
            '<p>{{ lang.text }}</p>'
            '{% endfor %}',
            {'text_phrases': phrases}
        )
        self.assertEqual(rendered, '',
                         'multi_text_phrase templatetag does not work')
