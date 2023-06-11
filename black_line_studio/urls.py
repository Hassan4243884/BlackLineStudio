from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.generic import TemplateView

from wagtail.admin import urls as wagtailadmin_paths
# from wagtail import paths as wagtail_paths
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_paths
from wagtail.contrib.sitemaps.views import sitemap

from home.views import RobotsView
from search import views as search_views

urlpatterns = [

    #Redirects
    path(r'contact-us/cf-shops-don-mills/', RedirectView.as_view()),
    path(r'contact-us/573-king-street-west-downtown/', RedirectView.as_view()),
    #Redirects

    path('sitemap.xml', sitemap),
    path(r'robots.txt', RobotsView.as_view(), name='robots'),
    path(r'django-admin/', admin.site.urls),

    path(r'admin/', include(wagtailadmin_paths)),
    path(r'documents/', include(wagtaildocs_paths)),

    path(r'search/', search_views.search, name='search'),
    path(r'', include('blog.urls', namespace="blog")),
    path(r'404/', TemplateView.as_view(template_name='404.html')),
    path(r'blog/', include('blog.urls', namespace="blog")),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path(r'', include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    path(r'pages/', include(wagtail_urls)),
]


# if settings.DEBUG:
#     from django.urls.static import static
#     from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#
#     # Serve static and media files from development server
#     urlpatterns += staticfiles_urlpatterns()
#     urlpatterns += static(settings.MEDIA_path, document_root=settings.MEDIA_ROOT)
