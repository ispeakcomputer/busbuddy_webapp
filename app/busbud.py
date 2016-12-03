'''
Title: Bus Buddy

Descroption: A little app that pulls RTD data and so always knows your bus arrival time

Author: Ryan Wright
'''

from google.transit import gtfs_realtime_pb2
import requests
from mylogins import *
import time

class Tripsdata:
    def __init__(self):
         self.count = 0
    def pull(self):
        '''Pull rtd-denver GTFS data and the assign bindings using gtfs_realtime_pb2'''
        global count
        while self.count == self.count:
            tufeed = gtfs_realtime_pb2.FeedMessage()
            print "Pulling the feed"
            response = requests.get('http://www.rtd-denver.com/google_sync/TripUpdate.pb', auth=(username, passwords))
            #Use response.content to load the binary into the feed object using gtfs_realtime_pb2 here.
            tufeed.ParseFromString(response.content)
            if tufeed == False:
                print "nothing loaded"
            else:
                print "Feed is loaded now"

            return tufeed
            time.sleep(30)
            count += 1
data = Tripsdata()


class Findarrival:
    def list(self, tufeed):
        self.times = []
        '''Now we loop through and find our bus and the stop that we need'''
        for entity in tufeed.entity:
            #for mytrip in entity.trip_update.stop_time_update:
            if entity.trip_update.trip.route_id == "0":
                for mystop in entity.trip_update.stop_time_update:
                    if mystop.stop_id == str("17780"):
                        #print mystop.arrival.time
                        self.times.append(mystop.arrival.time)

                        # p?rint "Arrival Time", self.convertedtime
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
                convertedlist = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(entry))
            return convertedlist
        else:
            convertedlist = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ournexttime))
            return convertedlist

convertedtimes = Converttime()

def main():
    # Pull the protocol buffer data and bindings
    feed = data.pull()

    # Feed this in to pull out our bus and stop times.This should be a list
    listoftimes = arrival.list(feed)
    for entry in listoftimes:
        print "looping through in main", entry

    # feed list in and find the smallest one
    mynextbus = ournextarrival.mintime(listoftimes)
    print "min time of that list", mynextbus

    mynextbusconverted = convertedtimes.converter(mynextbus)
    print "My next bus converted", mynextbusconverted

    myconvertedtimes = convertedtimes.converter(listoftimes)
    print "converted time in list of times:", myconvertedtimes

# Fire this baby off right here
main()
