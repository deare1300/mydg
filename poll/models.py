'''
Created on 2013-11-12

@author: Administrator
'''
from django.db import models

class User(models.Model):
    username=models.CharField(max_length=20,primary_key=True)
    password=models.DateField()
class LoginHistory(models.Model):
    username=models.ForeignKey(User)
    datetime=models.DateTimeField('date published')
    
from django.forms import ModelForm

class UserForm(ModelForm):
    pass