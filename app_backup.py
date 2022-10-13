from flask import Flask, render_template, request, redirect
from busbud import *

app = Flask(__name__)

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
    print "bus ", bus
    if len(bus) > 6:
        return render_template('warning.html')
    print "stop", stop
    if len(stop) > 6:
        return render_template('warning.html')
    thelist = data.pull()
    listoftimes = arrival.list(thelist, bus, stop)
    list = convertedtimes.converter(listoftimes)

    return render_template('arrivals.html', list=list, bus=bus, stop=stop)

if __name__ == '__main__':
  app.run(debug=True)
