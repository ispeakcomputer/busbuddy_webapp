from google.transit import gtfs_realtime_pb2
import requests
from mylogins import *
import time
from models import *

class Tripsdata:
    def __init__(self):
         self.count = 0
         self.datastore = self.pull

    def pull(self):
        '''Pull rtd-denver GTFS data and the assign bindings using gtfs_realtime_pb2'''

        tufeed = gtfs_realtime_pb2.FeedMessage()
        print "pulling data"
        try:
            response = requests.get('http://www.rtd-denver.com/google_sync/TripUpdate.pb', auth=(username, passwords))

        except requests.exceptions.Timeout:
            print "RTD Denver Data Timeout Trying Again In 60 Seconds"

        except requests.exceptions.TooManyRedirects:
            print "Too Many Redirects Trying Again In 60 Seconds"


        except requests.exceptions.RequestException as e:
            print str(e) + " Trying again in 60 Seconds"

        except requests.exceptions.HTTPError as err:
            print err

        tufeed.ParseFromString(response.content)
        print "Parsing Data"
        return tufeed

data = Tripsdata()

class Feedstore:
    def get_packaged_data(self, tufeed):
        '''Parse through RTD data and start loading it into database'''
        model_thing.renew()

        for entity in tufeed.entity:
            for mystop in entity.trip_update.stop_time_update:
                bus = entity.trip_update.trip.route_id
                print "Adding to Table to be commited later"
                print bus
                stop = mystop.stop_id
                print stop
                times = mystop.arrival.time
                print times

                model_thing.add(bus, stop, times)

        print "We will now make a big commit with all our data. This may take awhile"

        model_thing.commit()

feed = Feedstore()
