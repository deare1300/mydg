'''
Created on 2013-11-12

@author: Administrator
'''
from django.http import HttpResponse
import datetime


from django.shortcuts import render_to_response
from poll.models import User

def index(request):
    now = datetime.datetime.now()
    html = "<html><body><h3>Hello World!</h3>It is now %s </body></html>" % now
    return HttpResponse(html)


