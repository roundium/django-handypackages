from django.conf import settings
from django.template import Context, Template
from django.test import RequestFactory, TestCase
from django.urls import reverse


class ContextProcessorsTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def render_template(self, string, context=None):
        context = context or {}
        context = Context(context)
        return Template(string).render(context)

    def test_pass_data_cp(self):
        response = self.client.get(reverse('admin:index'), follow=True)
        self.assertEqual(
            response.context['default_language'],
            settings.LANGUAGE_CODE,
            'pass_data context processor does not work',
        )
