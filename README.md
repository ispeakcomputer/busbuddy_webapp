# Bus Buddy Flask App - Arrive On Time

This application pulls the real time data from Denvers RTD transit system.Website users request bus times from the database using the interface in order to find their stops next arrival times. The application finds the arrival times of all the buses on the road and stores them in the database. Data pulling, parsing, and the loading of the database is handled in the background with Celery task manager. RabbitMQ is used for messaging. Gunicorn serving our webpage. 

# Motivation

I wanted a more up to date bus arrival times using RTD's predictive data. 

# Installation

### Sqlite is enabled in models.py to allow testing of the app. Uncomment the Postgres SQLAlchemy ORM connection strings when ready for a production enviroment.

1. Download the content of the repo
2. Install Virtualenv
3. Activate Virtualenv to install enviroment in. See Virtualenv Docs for information
4. Run "$ pip install -r requirements.txt" to install everything needed to run the app
5. Make sure RabbitMQ is running "$sudo service rabbitmq-server restart"
6. Start Celery workers. I use "$celery -A __init__.celery -l info". I would suggest you find which way workers best suit your needs
7. Start Gunicorn with "$ gunicorn __init__:app"

