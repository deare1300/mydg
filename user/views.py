'''
Created on 2013-11-12

@author: Administrator
'''
from django.shortcuts import render
#from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from user.models import Person
from django.shortcuts import render_to_response,RequestContext
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
from user.models import LoginForm
import datetime
#from user.models import Person
from user.models import before_Login


from django.db.models.signals import pre_delete
from django.contrib.sessions.models import Session
from user.models import Logged

def sessionend_handler(sender, **kwargs):
    # cleanup session (temp) data
    print "session %s ended" % kwargs.get('instance').session_key
pre_delete.connect(sessionend_handler, sender=Session)

@csrf_protect
def index(request):    
    if 'username' in  request.session: 
        print "has username"     
        if 'person' in request.session:      
            count=online_total()
            person=request.session['person']
            print '-----------------------------:'+str(count),person,person.session_key,request.session.session_key
            if person.session_key==request.session.session_key and person.is_last():
                all_user=Person.objects.all()
                return render_to_response('user/welcome.html',{'username':request.session['username'],'total_user':count,'all_user':all_user})
            else:
                print "once again"
                del request.session['username']
                HttpResponseRedirect('user/index1.html')
    if  (request.method=='post' or request.method=="POST")   :       
        if  request.session['randint']==int(request.POST['randint']):        
            print '---------------------------------------int post',request.session['randint']
            
            username=request.POST['username']
            password=request.POST['password']
            form=LoginForm(request.POST)
            if form.is_valid():
                person=valid_login(request, request.POST['username'], request.POST['password'])
                if person:
                    #from user.models import process_request
                    #process_request(request)
                    person.session_key=request.session.session_key
                    request.session['username']=username
                    request.session['person']=person
                    count=online_total()
                    
                    person.save()
                    all_user=Person.objects.all()
                    request.session['randint']=None
                    return render_to_response('user/welcome.html',{'username':request.session['username'],'total_user':count,'all_user':all_user})
                else:
                    error="wrong username or password"
        else:
            print request.session['randint'],request.POST['randint']
    
    form=LoginForm()
    username=""
    password=""
    error="" 
    import random 
    randint=random.randint(0,1000)
    request.session['randint']=randint
    return render_to_response('user/index1.html',{'randint':randint,'username':username,"password":password,"error":error,"form":form},context_instance=RequestContext(request))
    
def valid_login(request,username,password):
    '''
    sql="select * from user_person where login=%s and password=%s" %(username,password)
    if Person.objects.raw(sql):
        return True
    return False
    '''
    #or
    try:
        result=Person.objects.filter(Q(login=username),password=password)
        if result:
            return result[0]
        else:
            return False
    except:
        return False
def logout(request):
    if request.session.get('username',False):
        del request.session['username']
        
    ##use the name of the url not the absolute path
    from django.core.urlresolvers import reverse   
    return HttpResponseRedirect(reverse('user_index'))


def online_total():
    i=0
    username=[]
    sessions= Session.objects.filter(expire_date__gte = datetime.datetime.now())
    for session in sessions:
        online_session=session.get_decoded().get('username',None)
        if online_session:
            print online_session
            username.append(online_session)
            i+=1
    return len(Person.objects.filter(login__in=username))
    return i
from django.core.signals import request_finished
from django.dispatch import receiver

'''
@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("------------ Request finished!-------------",sender)
    
    
'''
#
        
    