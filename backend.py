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
            # print "tufeed loaded"

            # make sure we loaded data from denver RTD API
            if tufeed == False:
                # print "nothing loaded from Denver RTD retrying in 10 seconds"
                time.sleep(10)


            else:
                print "Feed is loaded now"
                self.count += 1
                # print self.count
                return tufeed
                # print "Pulled the feed %s time and stored in data.datastore" %count
                # time.sleep(60)
                # time.sleep(60)
                # pass
data = Tripsdata()

class Feedstore:
    def get_packaged_data(self, tufeed):
        self.times = []
        # print "bus inside func", bus
        # self.bus = bus
        # self.stop = stop
        '''Now we loop through and find our bus and the stop that we need'''
        for entity in tufeed.entity:
            # print entity
            # print "stop inside func", stop
            #for mytrip in entity.trip_update.stop_time_update:
            for bus in entity.trip_update.trip.route_id:
                # print "bus matches"
                print "This is the bus right here ---->", bus
                for mystop in entity.trip_update.stop_time_update:
                    print "This is the stop right here ------>", mystop
                    # if mystop.stop_id == stop:
                        # print "stop matches"
                        #print mystop.arrival.time
                    self.times.append(mystop.arrival.time)
        # for i in self.times:
        #     print self.time['i']
        return self.times
feed = Feedstore()


class Findarrival:
    def list(self, tufeed, bus, stop):
        self.times = []
        # print "bus inside func", bus
        # self.bus = bus
        # self.stop = stop
        '''Now we loop through and find our bus and the stop that we need'''
        for entity in tufeed.entity:
            # print entity
            # print "stop inside func", stop
            #for mytrip in entity.trip_update.stop_time_update:
            if entity.trip_update.trip.route_id == bus:
                # print "bus matches"
                for mystop in entity.trip_update.stop_time_update:
                    if mystop.stop_id == stop:
                        print "stop matches"
                        #print mystop.arrival.time
                        self.times.append(mystop.arrival.time)
        # for i in self.times:
        #     print self.time['i']
        return self.times
arrival = Findarrival()

if __name__ == '__main__':
    ourdata = data.pull()
    db_data = feed.get_packaged_data(ourdata)
    # db_data = arrival.list(data , '0', '14986')
    print(db_data)
