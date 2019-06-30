from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Product


class ProductSitemap(Sitemap):
    r"""
        from django.contrib.sitemaps.views import sitemap
        from handypackages.blog.sitemap_view import BlogSitemap

        sitemaps = {
            'product': ProductSitemap(url_name='public:sitemap'),
        }


        urlpatterns = [
            url(r'^admin/', admin.site.urls),
            url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
                name='django.contrib.sitemaps.views.sitemap'),

    """

    changefreq = "daily"
    priority = 0.1
    model = Product

    def __init__(self, url_name=None):
        super(ProductSitemap, self).__init__()
        if not url_name:
            raise Exception('url_name argument missed for Product Sitemap')
        self.url_name = url_name

    def items(self):
        return self.model.all()

    def lastmod(self, obj):
        return obj.create_time

    def location(self, obj):
        return reverse(self.url_name, kwargs={'slug': obj.slug})
