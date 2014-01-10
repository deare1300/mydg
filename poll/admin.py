'''
Created on 2013-11-12

@author: Administrator
'''
from django.contrib import admin
from poll.models import User
from user.models import Person
#admin.site.register(User)

class PollAdmin(admin.ModelAdmin):
    fields=['username']
    
admin.site.register(User, PollAdmin)
#admin.site.register(Person)