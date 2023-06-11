from django.urls import path, re_path
from . import views


app_name = 'blog'

urlpatterns = [
    path('tag/<slug:tag>/', views.tag_view, name="tag"),
    path('category/<slug:category>/feed/', views.LatestCategoryFeed(), name="category_feed"),
    path('category/<slug:category>/', views.category_view, name="category"),
    path('author/<slug:author>/', views.author_view, name="author"),
    re_path(r'(?P<blog_slug>[\w-]+)/rss.*/', views.LatestEntriesFeed(), name="latest_entries_feed"),
    re_path(r'(?P<blog_slug>[\w-]+)/atom.*/', views.LatestEntriesFeedAtom(), name="latest_entries_feed_atom"),
]
