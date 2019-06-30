from django import template

from .nodes import (FacebookShareLinkCreatorNode, TelegramShareLinkCreatorNode,
                    TwitterShareLinkCreatorNode,)

register = template.Library()


@register.tag(name='facebook_share')
def generate_facebook_share_link(parser, token):
    """
    generate share link for facebook
    example:
        {% load link_creators %}
        <a href="{% facebook_share "django" "https://djangoproject.com/" %}">
        share in facebook
        </a>
    """
    try:
        tag_name, title, link = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            '%r tag requires two argument' % token.contents.split()[0]
        )
    return FacebookShareLinkCreatorNode(link, title)


@register.tag(name='twitter_share')
def generate_twitter_share_link(parser, token):
    """
    generate share link for twitter
    example:
        {% load link_creators %}
        {% twitter_share "django" "https://google.com/" "django,python" %}"
        share in facebook
        </a>
    """
    try:
        tag_name, text, link, hashtags = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            '%r tag requires two argument' % token.contents.split()[0]
        )
    return TwitterShareLinkCreatorNode(text, link, hashtags)


@register.tag(name="telegram_share")
def generate_telegram_share_link(parser, token):
    """
    generate share link for telegram
    example:
        {% load link_creators %}
        {% telegram_share "learn django" "https://djangoproject.com/" %}"
        share in Telegram
        </a>
    """
    try:
        tag_name, text, link = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            '%r tag requires two argument' % token.contents.split()[0]
        )
    return TelegramShareLinkCreatorNode(text, link)
