from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.generic import TemplateView


from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.contrib.sitemaps.views import sitemap

from home.views import RobotsView
from search import views as search_views

urlpatterns = [

    #Redirects
    url(r'^contact-us/cf-shops-don-mills/$', RedirectView.as_view(url='/contact-us/', permanent=True)),
    url(r'^contact-us/573-king-street-west-downtown/$', RedirectView.as_view(url='/contact-us/', permanent=True)),
    #Redirects

    url('^sitemap\.xml$', sitemap),
    url(r'^robots\.txt$', RobotsView.as_view(), name='robots'),
    url(r'^django-admin/', admin.site.urls),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', search_views.search, name='search'),
    url(r'^', include('blog.urls', namespace="blog")),
    url(r'^404/$', TemplateView.as_view(template_name='404.html')),
    # url(r'^blog/', include('blog.urls', namespace="blog")),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r'', include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r'^pages/', include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)