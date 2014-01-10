'''
Created on 2013-11-13

@author: Administrator
'''
from django.conf.urls import patterns, url
from gateway import views

urlpatterns=patterns('',
                     url(r'^$',views.index,name='index'),
                     url(r'^index/$',views.index),
                   
                     )