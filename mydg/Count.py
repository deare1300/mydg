'''
Created on 2013-12-23

@author: Administrator
'''
from threading import Thread
from random import randint
from time import sleep
class Count(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.count=randint(0,1000)
        print "apapapaap " + str(self.count)
    def run(self):
        while True:
            try:
                sleep(10)
                #self.count+=1
            except:
                continue