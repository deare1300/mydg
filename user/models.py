'''
Created on 2013-11-12

@author: Administrator
'''
from django.db import models
from django import forms
from django.forms import ModelForm
from django.db.models.signals import pre_delete
from django.contrib.sessions.models import Session

from django.contrib.auth.signals import user_logged_in


def sessionend_handler(sender, **kwargs):
    # cleanup session (temp) data
    print "session %s ended" % kwargs.get('instance').session_key
pre_delete.connect(sessionend_handler, sender=Session)
class Person(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=40)
    login=models.CharField(max_length=40)
    password=models.CharField(max_length=40)
    session_key=models.CharField(null=True, blank=True,max_length=100)
    def is_last(self):
        last_session_person=Person.objects.get(login=self.login)
        print 'in last_-----------------',last_session_person,last_session_person.session_key
        return  last_session_person.session_key==self.session_key
    


class LoginForm(forms.Form):
    username=forms.CharField(max_length=20,required=True)
    password=forms.CharField(widget=forms.PasswordInput,required=True)
   # password=forms.CharField(max_length=20,required=True)


    
#############the signals exmaple ###################


#from user.signal import delete_done
#import logging
###first create a signal=======================
import django.dispatch
delete_done=django.dispatch.Signal(providing_args=['obj'])

##### then create the sender of the signal #########
class Article(models.Model):
    title=models.CharField(max_length=10)
    def delete(self):
        delete_done.send(sender=Article,obj=self)
## then create the reciver of the signal        
def known(sender,**kwargs):
    print '-------------'
    if 'obj' in kwargs:
        print 'yes'
        obj=kwargs.get('obj')
        
        print obj
        print obj.title
    print ('signal recieved!!!!!!')

## connect the sender and reciever of the signal
delete_done.connect(known, sender=Article)


def Logged(session):
    sessions=Session.objects.filter(expire_date__gte = datetime.datetime.now())
    return session in sessions and session
import datetime
def  before_Login(username):
    print 'before LOGIN'
    sessions= Session.objects.filter(expire_date__gte = datetime.datetime.now())
    print len(sessions)
    i=0
    for session in sessions:
        session=session.get_decoded()
        name=session.get('username',False)
        if  name==username:
            del session
            print 'delete',sessions
        i+=1
        
def process_request( request):
    cur_session_key = request.user.visitor.session_key
    if cur_session_key and cur_session_key != request.session.session_key:
        Session.objects.filter(session_key=cur_session_key).delete()
    request.user.visitor.session_key = request.session.session_key
    request.user.visitor.save()        
