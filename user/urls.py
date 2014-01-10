'''
Created on 2013-11-12

@author: Administrator
'''
from django.conf.urls import patterns, url
from user import views

urlpatterns=patterns('',
                     url(r'^$',views.index,name='user_index'),
                     url(r'^index/$',views.index),
                     url(r'^logout/$',views.logout,name='user_logout'),
                      #url(r'^index/$',views.index),
                  #  url(r'(?P<poll_id>\w+)/$',views.detail, name='detail'),
                 #    url(r'(?P<poll_id>\d+)/results/$',views.results,name='results')
                     )
