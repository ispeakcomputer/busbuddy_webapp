# Bus Buddy Flask App - Arrive On Time

![Image]()
<a href="https://github.com/ispeakcomputer/busbuddy_webapp/blob/master/images/busbuddy_image.png" title="app image"><img src="https://github.com/ispeakcomputer/busbuddy_webapp/blob/master/images/busbuddy_image.png" width="500"></a>
This application pulls the real time data from Denvers RTD transit system. Website users request bus times from the database using the interface in order to find their stops next arrival times. 

This app is different because you can approch in the stop number and get exact times for that stop.

The application finds the arrival times of all the buses for the day and stores them in the database. Data pulling, parsing, and the loading of the database is handled in the background with Celery task manager. RabbitMQ is used for messaging. Gunicorn serving our webpage.

# Motivation

I wanted a more up to date bus arrival times using RTD's predictive data because the existing app was lacking.

# Installation

1. Navigate into the busbuddy_webapp directory
2. Install pip and virtualenv with "sudo apt-get install pip virtualenv"
3. Set up your virtualenv directory and activate it. See virtualenv documentation. 
4. run "pip install -r requirements.txt" to install the needed packages.
5. run "chmod +x start_service.sh stop_service to run start and stop script locally 
6. run ./start_service.sh to start app. Wait for the app to come up and load database. 
7. run ./stop_service.sh to stop the messaging queue, celery and gunicorn completely.
