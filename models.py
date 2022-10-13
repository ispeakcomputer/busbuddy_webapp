from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from mylogins import endpoint

app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# This will work for our production postgres db
# app.config ['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://ryan:database666@busdatabase.cjjoqnd9i3es.us-west-2.rds.amazonaws.com:5432/busdb'

db = SQLAlchemy(app)

class Mymodel(db.Model):
    __tablename__ = 'bus_table'
    id = db.Column(db.Integer, primary_key=True)
    bus = db.Column(db.String(10))
    stop = db.Column(db.String(10))
    times = db.Column(db.String(50), )

    def __init__(self, bus, stop, times ):
        '''now load model stuff into objects that you can play with'''
        self.bus = bus
        self.stop = stop
        self.times = times

    def __repr__(self):
        return '<Bus %r><Stop %r><Times %r>' %self.bus %self.stop %self.times

class Database_actions():

    def get(self, bus, stop):
        list = []
        self.bus = bus
        self.stop = stop
        print "Database_actions.get for", self.bus
        print "Database_actions.get for", self.stop
        # Limiting this greatly reduces timeit
        buses = Mymodel.query.order_by(Mymodel.times).filter_by(bus=self.bus).filter_by(stop=self.stop).all()

        for i in buses:
            print "This is our test", i.times
            list.append(i.times)

        return list

    def add(self, load_bus, load_stop, load_times):
        ''' Load the row into the database '''

        self.bus_input = load_bus
        self.stop_input = load_stop
        self.times_input = load_times

        new_entry = Mymodel(bus=self.bus_input, stop=self.stop_input , times=self.times_input )

        print "Going into database"
        print  self.bus_input + ' ' + self.stop_input + ' ' + str(self.times_input)

        db.session.add(new_entry)

    def renew(self):
        Mymodel.query.delete()

        print "Dropped and Created Table.....done"

    def commit(self):
        db.session.commit()
        print "Commited new times"

model_thing = Database_actions()

if __name__ == "__main__":
    app.run(debug=True)
