'''
Created on 2013-11-15

@author: Administrator
'''
import django.dispatch
delete_done=django.dispatch.Signal(providing_args=['obj'])
