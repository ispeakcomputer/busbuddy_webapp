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
        nexttime = min(time)
        return nexttime
ournextarrival = Nextarrival()

class Converttime:
    def converter(self, ournexttime):
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
