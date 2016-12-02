'''
Title: Bus Buddy

Descroption: A little app that pulls RTD data and so always knows your bus arrival time

Author: Ryan Wright
'''

from google.transit import gtfs_realtime_pb2
import requests
from mylogins import *
import time

count = 0

def gettripupdate():
    '''Pull rtd-denver GTFS data and the assign bindings using gtfs_realtime_pb2'''
    global count
    while count == count:
        tufeed = gtfs_realtime_pb2.FeedMessage()
        print "Pulling the feed"
        response = requests.get('http://www.rtd-denver.com/google_sync/TripUpdate.pb', auth=(username, passwords))
        #Use response.content to load the binary into the feed object using gtfs_realtime_pb2 here.
        tufeed.ParseFromString(response.content)
        if tufeed == False:
            print "nothing loaded"
        else:
            print "Feed is loaded now"


        findarrival(tufeed)
        time.sleep(30)
        count += 1

def findarrival(tufeed):
    times = []
    '''Now we loop through and find our bus and the stop that we need'''
    for entity in tufeed.entity:
        #for mytrip in entity.trip_update.stop_time_update:
        if entity.trip_update.trip.route_id == "0":
            for mystop in entity.trip_update.stop_time_update:
                if mystop.stop_id == str("17780"):
                    #print mystop.arrival.time
                    times.append(mystop.arrival.time)
                    convertedtime = converttime(mystop.arrival.time)
                    print "Arrival Time", convertedtime
    findnextarrival(times)
                #print "each route discription", mytrip

def findnextarrival(times):
    ''' We simply find the lowest POSIX time and this will be our next bus'''
    nexttime = min(times)
    print "The next bus will be at it's stop at ", converttime(nexttime)

def converttime(ournexttime):
    '''Here we convert the POSIX time from our GTFS feed to a date and time that we can read'''
    convertedtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ournexttime))
    return convertedtime


def main():
    gettripupdate()

main()
