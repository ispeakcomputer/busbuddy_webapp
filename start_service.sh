#!/bin/bash

#Get RabbitMQ going
echo Now we will start RabbitMQ
sleep 5
sudo service rabbitmq-server restart

#Run Celery
echo lets start Celery now
sleep 5
sudo celery -A __init__.celery -l info

#Run Gunicorn
echo Lets now start Gunicorn
 sleep 5
sudo gunicorn __init__:app
