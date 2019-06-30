from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils.feedgenerator import Atom1Feed

from handypackages.blog.models import Blog


class BlogFeed(Feed):
    """
    example default:
        url(
            "^rss/$",
            BlogFeed(
                limit=50,
                url_name="public:blog-single",
                link=reverse_lazy("blog-feed-default"),
                title="Blog Site Title",
                description="Site Blog Feed"
            ),
            name="blog-feed-default"
        )
    example atom:
        url(
            "^atom/$",
            BlogFeed(
                limit=50,
                url_name="public:blog-single",
                link=reverse_lazy("blog-feed-atom"),
                title="Blog Site Title",
                description="Site Blog Feed",
                feed_type="atom"
            ),
            name="blog-feed-atom"
        )
    """
    model = Blog

    def __init__(
            self, limit=20, title="Blog Feed", link="/blog-feed/",
            url_name=None, description="Site BLog Feed", feed_type="default"):
        super(BlogFeed, self).__init__()
        self.limit = limit
        self.title = title
        self.link = link
        self.description = description
        self.url_name = url_name
        if not self.url_name:
            raise Exception("url_name argument missed!")
        if feed_type == "atom":
            self.feed_type = Atom1Feed

    def items(self):
        return self.model.published.all()[:self.limit]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_link(self, item):
        return reverse(self.url_name, args=[item.slug])
