'''
Created on 2013-11-13

@author: Administrator
'''
from django.db import models
class Deploy(models.Model):
    ip=models.IPAddressField()
    port=models.IntegerField()
    introduce=models.CharField()