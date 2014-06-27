from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from django.conf.urls.static import static

from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PoolsideTrackLister.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', 'ListTracks.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += patterns('',
        url(settings.STATIC_URL, settings.STATIC_ROOT),
        url(settings.MEDIA_URL, settings.MEDIA_ROOT),
        url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    )
