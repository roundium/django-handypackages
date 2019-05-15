from django import template
from django.template.defaultfilters import urlencode


class FacebookShareLinkCreatorNode(template.Node):
    url = "https://www.facebook.com/sharer/sharer.php?u=%s&t=%s"

    def __init__(self, link, title):
        self.link = link[1:-1]
        self.title = title[1:-1]

    def render(self, context):
        return self.url % (
            urlencode(self.link),
            urlencode(self.title)
        )


class TwitterShareLinkCreatorNode(template.Node):
    url = "https://twitter.com/share?text=%s&url=%s&hashtags=%s"

    def __init__(self, text, link, hashtags):
        self.text = text[1:-1]
        self.link = link[1:-1]
        self.hashtags = hashtags[1:-1]

    def render(self, context):
        return self.url % (
            urlencode(self.text),
            urlencode(self.link),
            self.hashtags
        )
