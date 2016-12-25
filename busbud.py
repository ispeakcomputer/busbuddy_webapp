'''
Title: Bus Buddy

Description: This handles everything for this app that the database script(models.py) or our routes script(__init__)
             doesn't do.

Author: Ryan Wright
'''
from google.transit import gtfs_realtime_pb2
import requests
from mylogins import *
import time

class Nextarrival:
    def mintime(self, time):
        self.times = []
        ''' We simply find the lowest POSIX time and this will be our next bus'''
        nexttime = min(time)
        return nexttime
ournextarrival = Nextarrival()

class Converttime:
    def converter(self, ournexttime):
        '''Here we convert the POSIX time from our GTFS feed to a date and time that we can read
        We try and detect a list as well as a single var so we can use many different inputs'''
        self.times = ournexttime
        convertedlist = []
        if type(self.times) is list:
            for entry in self.times:
                converttime = time.strftime('%I:%M %p (%Y-%m-%d)', time.localtime(float(entry)))
                convertedlist.append(converttime)
            return convertedlist
        else:
            convertedlist = time.strftime('%I:%M %p (%Y-%m-%d)', time.localtime(ournexttime))
            # print "converting single instead"
            return convertedlist

class Checkinput:
    def __init__(self):
         self.digits = 6
    def checker(self, bus, stop):
        ''' Check to make sure input isn't over 6 digits '''
        if len(bus) > self.digits:
            return False
        else:
            pass

        if len(stop) > self.digits:
            return False
        else:
            pass

        return True

convertedtimes = Converttime()
