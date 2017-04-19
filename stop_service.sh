#!/bin/bash


echo Killing Celery Workers
sudo kill -9 `ps -ef | grep celery | grep -v grep | awk '{print $2}'`
sleep 3
echo Checking if any celerys are still 
echo
ps -aux|grep celery


echo Killing RabbitMQ
sudo kill -9 `ps -ef | grep rabbitmq | grep -v grep | awk '{print $2}'`
sleep 3
echo Checking to see if RabbitMQ is still running.
echo


ps -aux|grep rabbitmq


echo Killing Gunicorn
sudo kill -9 `ps -ef | grep gunicorn | grep -v grep | awk '{print $2}'`
sleep 3
ps -aux|grep gunicorn


echo KILL ANY PROCESSES LEFT OVER WITH KILL !
