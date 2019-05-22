from django import template

from .nodes import FacebookShareLinkCreatorNode, TwitterShareLinkCreatorNode

register = template.Library()


@register.tag(name="facebook_share")
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
            "%r tag requires two argument" % token.contents.split()[0]
        )
    return FacebookShareLinkCreatorNode(link, title)


@register.tag(name="twitter_share")
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
            "%r tag requires two argument" % token.contents.split()[0]
        )
    return TwitterShareLinkCreatorNode(text, link, hashtags)
