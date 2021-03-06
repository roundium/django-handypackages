import os
import datetime

from django.template import Context, Template, TemplateSyntaxError
from django.template.defaultfilters import urlencode
from django.test import TestCase


class TemplateTagsTests(TestCase):
    def render_template(self, string, context=None):
        context = context or {}
        context = Context(context)
        return Template(string).render(context)

    def test_google_analytic_tag(self):
        self.assertRaises(
            Exception,
            self.render_template,
            string='{% load google_analytic %}'
            '{% google_analytic %}'
        )

        rendered = self.render_template(
            '{% load google_analytic %}'
            '{% google_analytic "UA-515165812" %}'
        )
        correct_response = '<script>' + os.linesep + "    " +\
        r'function gtag(){dataLayer.push(arguments)}window.dataLayer=window.dataLayer||[],gtag("js",new Date),gtag("config","UA-515165812");' +\
        os.linesep + '</script>' + os.linesep + r'<script async src="https://www.googletagmanager.com/gtag/js?id=UA-515165812"></script>' + os.linesep +\
        r'<script async src="https://www.google-analytics.com/analytics.js"></script>' + os.linesep
        self.assertEqual(rendered, correct_response,
                         'google analytic tag does not work!')

    def test_facebook_share_link_creator(self):
        self.assertRaises(
            TemplateSyntaxError,
            self.render_template,
            '{% load link_creators %}'
            '{% facebook_share %}'
        )
        rendered = self.render_template(
            '{% load link_creators %}'
            '{% facebook_share "django" "https://djangoproject.com/" %}'
        )
        self.assertEqual(
            rendered,
            'https://www.facebook.com/sharer/sharer.php?u=%s&t=%s' % (
                urlencode('https://djangoproject.com/'),
                urlencode('django')
            ),
            'Facebook share link creator not working!'
        )

    def test_twitter_share_link_creator(self):
        self.assertRaises(
            TemplateSyntaxError,
            self.render_template,
            '{% load link_creators %}'
            '{% twitter_share %}'
        )
        rendered = self.render_template(
            '{% load link_creators %}'
            '{% twitter_share "django" "https://djangoproject.com/" "django,python,pypy" %}'
        )
        self.assertEqual(
            rendered,
            'https://twitter.com/share?text=%s&url=%s&hashtags=%s' % (
                urlencode('django'),
                urlencode('https://djangoproject.com/'),
                'django,python,pypy'
            ),
            'Facebook share link creator not working!'
        )

    def test_telegram_share_link_creator(self):
        self.assertRaises(
            TemplateSyntaxError,
            self.render_template,
            '{% load link_creators %}'
            '{% telegram_share %}'
        )
        rendered = self.render_template(
            '{% load link_creators %}'
            '{% telegram_share "django" "https://djangoproject.com/" %}'
        )
        self.assertEqual(
            rendered,
            'https://telegram.me/share/url?url=%s&text=%s' % (
                urlencode('https://djangoproject.com/'),
                urlencode('django'),
            ),
            'Telegram share link creator not working!'
        )

    def test_date_time_conv(self):
        self.assertRaises(
            TemplateSyntaxError,
            self.render_template,
            '{% load date_time_conv %}'
            '{{ "datetime"|persian_datetime:"%y/%m/%d" }}',
        )

        rendered = self.render_template(
            '{% load date_time_conv %}'
            '{{ datetime|persian_datetime:"%y/%m/%d" }}',
            {"datetime": datetime.datetime(2019, 5, 28)}
        )
        self.assertEqual(
            rendered,
            "1398/3/7"
        )

        rendered = self.render_template(
            '{% load date_time_conv %}'
            '{{ datetime|persian_datetime:"%y/%m/%d %h:%M:%s" }}',
            {"datetime": datetime.datetime(2019, 5, 28, 1, 10, 33)}
        )
        self.assertEqual(
            rendered,
            "1398/3/7 1:10:33"
        )

        rendered = self.render_template(
            '{% load date_time_conv %}'
            '{{ datetime|persian_datetime:"%y %n %d" }}',
            {"datetime": datetime.datetime(2019, 5, 28, 1, 10, 33)}
        )
        self.assertEqual(
            rendered,
            "1398 خرداد 7"
        )
