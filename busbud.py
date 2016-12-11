'''
Title: Bus Buddy

Description: A little app that pulls RTD data and so always knows your bus arrival time

Author: Ryan Wright
'''
from google.transit import gtfs_realtime_pb2
import requests
from mylogins import *
import time

class Tripsdata:
    def __init__(self):
         self.count = 0
         self.datastore = self.pull
    def pull(self):
        '''Pull rtd-denver GTFS data and the assign bindings using gtfs_realtime_pb2'''
        while True:
            tufeed = gtfs_realtime_pb2.FeedMessage()
            response = requests.get('http://www.rtd-denver.com/google_sync/TripUpdate.pb', auth=(username, passwords))
            #Use response.content to load the binary into the feed object using gtfs_realtime_pb2 here.
            tufeed.ParseFromString(response.content)
            print "tufeed loaded"

            # make sure we loaded data from denver RTD API
            if tufeed == False:
                print "nothing loaded from Denver RTD retrying in 10 seconds"
                time.sleep(10)


            else:
                print "Feed is loaded now"
                self.count += 1
                print self.count
                return tufeed
                print "Pulled the feed %s time and stored in data.datastore" %count
                time.sleep(60)
                # time.sleep(60)
                # pass
data = Tripsdata()


class Findarrival:
    def list(self, tufeed, bus, stop):
        self.times = []
        print "bus inside func", bus
        # self.bus = bus
        # self.stop = stop
        '''Now we loop through and find our bus and the stop that we need'''
        for entity in tufeed.entity:
            print entity
            print "stop inside func", stop
            #for mytrip in entity.trip_update.stop_time_update:
            if entity.trip_update.trip.route_id == bus:
                print "bus matches"
                for mystop in entity.trip_update.stop_time_update:
                    if mystop.stop_id == stop:
                        print "stop matches"
                        #print mystop.arrival.time
                        self.times.append(mystop.arrival.time)
        # for i in self.times:
        #     print self.time['i']
        return self.times
arrival = Findarrival()
# arrival.list(tufeed)

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
                converttime = time.strftime('%I:%M %p (%Y-%m-%d)', time.localtime(entry))
                convertedlist.append(converttime)
            return convertedlist
        else:
            convertedlist = time.strftime('%I:%M %p (%Y-%m-%d)', time.localtime(ournexttime))
            print "converting single instead"
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
