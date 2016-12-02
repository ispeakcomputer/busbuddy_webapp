from flask import Flask, render_template, request, redirect

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
    return render_template('arrivals.html', bus=bus, stop=stop)
    # return "bus" + str(bus) + ' Route' + str(route)
    # return redirect('/')

  # return render_template('home.html')

if __name__ == '__main__':
  app.run(debug=True)
