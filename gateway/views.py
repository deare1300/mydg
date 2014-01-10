'''
Created on 2013-11-13

@author: Administrator
'''
from django.http import HttpResponse
from django.template import Context,loader
#from poll.models import User

from django.shortcuts import render


def index(request):
    return HttpResponse("fsfs")