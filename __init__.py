from flask import Flask, render_template, request, redirect
from busbud import *
from backend import Database_actions, model_thing

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'postgressql://khole:databa5318@localhost/busdb'


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

if __name__ == '__main__':
  app.run(debug=True)
