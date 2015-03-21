from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings 
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Ueditor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'ueditor.views.index', name='index'),
    url(r'^controller', 'ueditor.controller.Get_Actions'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)
