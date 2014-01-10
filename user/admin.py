'''
Created on 2013-11-12

@author: Administrator
'''
from django.contrib import admin
from user.models import Person
#admin.site.register(User)

class UserAdmin(admin.ModelAdmin):
    fields=['login','password']
    
admin.site.register(Person, UserAdmin)