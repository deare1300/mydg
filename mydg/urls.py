from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#from poll import urls
from mydg import views
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mydg.views.home', name='home'),
    # url(r'^mydg/', include('mydg.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', views.index),
    
     url(r'^admin/', include(admin.site.urls)),
   # url('^$','mydg.views.index'),
   url(r'^poll/',include("poll.urls")),
   url(r'^user/',include('user.urls')),
   url(r'gateway/',include('gateway.urls')),
)
urlpatterns+=patterns('',
                      url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.STATIC_URL, 'show_indexes': True})
                      )
