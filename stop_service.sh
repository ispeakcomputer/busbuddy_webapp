#!/bin/bash


echo Killing Celery Workers
sudo pkill -f celery
sleep 3
echo Checking if any celerys are still running that need to be killed
echo
ps -aux|grep celery


echo Killing RabbitMQ
sudo kill -9 `ps -ef | grep rabbitmq | grep -v grep | awk '{print $2}'`
sleep 3
echo Checking to see if RabbitMQ is still running. If so then kill the processes manualy
echo


ps -aux|grep rabbitmq


echo Killing Gunicorn
pkill -f gunicorn
sleep 3
ps -aux|grep gunicorn


echo KILL ANY PROCESSES LEFT OVER WITH KILL !
