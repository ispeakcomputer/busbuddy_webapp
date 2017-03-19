from flask import Flask, render_template, request, redirect
from busbud import *
from backend import Database_actions, model_thing, data, feed
from celery import Celery
import time

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://localhost//'
# app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post', methods=['POST'])
def post():
    bus = request.form['bus']
    stop = request.form['stop']
    checkinput = Checkinput()

    '''Check to see how many digits user is entering return warning over 6 digits'''
    if checkinput.checker(bus, stop) == False:
        return render_template('warning.html')
    else:
        '''Pull this data and start loading into the page'''
        print 'This is __init__ function' + bus + ' ' + stop
        listoftimes = model_thing.get(bus, stop)
        list = convertedtimes.converter(listoftimes)
        for i in range(len(list)):
            print list[i]
        return render_template('arrivals.html', list=list, bus=bus, stop=stop)

@celery.task
def reload_database():
    while True:
        ourdata = data.pull()
        feed.get_packaged_data(ourdata)
        print "The task ran I thinks"
        time.sleep(60)


reload_database.delay()

if __name__ == '__main__':
    print "Running if __name__ == '__main__ ' in __init__"

    # pull data to store in our database.

    app.run(debug=True)
