#Bus Buddy Flask App - Arrive On Time

This application pulls the real time data from Denvers RTD transit system. The application finds the arrival times of all the buses on the road and stores them in the database. Users request bus times from the database in order to find their stops next arrival times.

#Motivation

I wanted a more up to date bus arrival times using RTD's predictive data. 

#Modules Needed
gtfs_realtime_pb2
requests
time
pyscopg2
postgres
