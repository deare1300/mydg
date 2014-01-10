"""
WSGI config for mydg project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os
print '--------------WSGI1'

# We defer to a DJANGO_SETTINGS_MODULE already in the environment. This breaks
# if running multiple sites in the same mod_wsgi process. To fix this, use
# mod_wsgi daemon mode with each site in its own daemon process, or use
# os.environ["DJANGO_SETTINGS_MODULE"] = "mydg.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mydg.settings")
print '--------------WSGI2'

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
print '--------------WSGI3'
from time import sleep
from threading import Thread
from random import randint
print '--------------WSGI4'
'''
class Count(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.count=randint(0,1000)
    def run(self):
        while True:
            try:
                sleep(10)
                #self.count+=1
            except:
                continue
'''
'''
from mydg.Count import Count
print '--------------WSGI5'
my_count=Count()
print '--------------WSGI6'
my_count.start()
'''
# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)

    
