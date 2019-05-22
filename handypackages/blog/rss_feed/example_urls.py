from django.conf.urls import url
from django.urls import reverse_lazy

from .view import BlogFeed

urlpatterns = [
    url(
        "^rss/$",
        BlogFeed(
            limit=50,
            url_name="blog-single",
            link=reverse_lazy("blog-feed-default"),
            title="Blog Site Title",
            description="Site Blog Feed"
        ),
        name="blog-feed-default"
    ),
    url(
        "^atom/$",
        BlogFeed(
            limit=50,
            url_name="blog-single",
            link=reverse_lazy("blog-feed-atom"),
            title="Blog Site Title",
            description="Site Blog Feed",
            feed_type="atom"
        ),
        name="blog-feed-atom"
    ),
]
