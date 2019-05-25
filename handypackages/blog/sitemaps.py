from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Blog


class BlogSitemap(Sitemap):
    r"""
        from django.contrib.sitemaps.views import sitemap
        from handypackages.blog.sitemap_view import BlogSitemap

        sitemaps = {
            'blog': BlogSitemap(url_name='public:blog-single'),
        }


        urlpatterns = [
            url(r'^admin/', admin.site.urls),
            url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
                name='django.contrib.sitemaps.views.sitemap'),

    """

    changefreq = "hourly"
    priority = 0.3
    model = Blog

    def __init__(self, url_name=None):
        super(BlogSitemap, self).__init__()
        if not url_name:
            raise Exception("url_name argument missed for Blog Sitemap")
        self.url_name = url_name

    def items(self):
        return self.model.published.all()

    def lastmod(self, obj):
        return obj.publish_time

    def location(self, obj):
        return reverse(self.url_name, kwargs={'slug': obj.slug})
