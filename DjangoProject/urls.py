from django.conf.urls import patterns, include, url
from django.contrib import admin
from BrowseFile.view import first
from BrowseFile.view import MarkDir
from BrowseFile.view import OpenTxtPage

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    (r'^$', first),
    url(r'^MarkDir$', MarkDir),
    url(r'^OpenTxtPage', OpenTxtPage),
)
