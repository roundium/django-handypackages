from django import template

register = template.Library()


@register.inclusion_tag("handyutils/google-analytics.html")
def google_analytic(api_key=None):
    """
    generate google analytic html
    example:
        {% load google_analytic %}
        {% google_analytic "UA-111111111" %}
    """
    if not api_key:
        raise Exception('google api key is required.')
    return {
        'api_key': api_key
    }
