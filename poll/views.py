'''
Created on 2013-11-12

@author: Administrator
'''

from django.http import HttpResponse
from django.template import Context,loader
from poll.models import User

from django.shortcuts import render

from mydg.Count import Count
print '--------------1'
my_count=Count()
print '--------------2'
def index(request):
    #return HttpResponse("index")
    latest_poll_list=User.objects.all()
    '''
    template=loader.get_template('poll/index.html')
    context=Context({
                     'latest_poll_list':latest_poll_list,})
    return HttpResponse(template.render(context))
    '''
    #from mydg.wsgi import my_count
    print '----------------poll/index'
    context={'latest_poll_list':latest_poll_list,'count':my_count.count}
    return render(request,'poll/index.html',context)

def detail(request,poll_id):
    from django.http import Http404
    try:
        pass
    except:
        raise Http404
    return HttpResponse("You are looking at detail p0ll %s" % poll_id)

def results(request,poll_id):
    return HttpResponse("You are looking at p0ll results %s" % poll_id)

