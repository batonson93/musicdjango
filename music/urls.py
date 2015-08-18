from django.conf.urls import include, url, patterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', 'music.views.home', name='home'),
    url(r'^music/$', 'music.views.music', name='music'),
    url(r'^videos/$', 'music.views.videos', name='videos'),
    url(r'^blog/$', 'music.views.blog', name='blog'),
    url(r'^shop/$', 'music.views.shop', name='shop'),
    url(r'^tour/$', 'music.views.tour', name='tour'),
    url(r'^media/$', 'music.views.media', name='media'),
    url(r'^news/(?P<article_id>[0-9]+)/$', 'music.views.show_news', name="news"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)