from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://khole:databa5318@localhost/busdb'
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
        db.drop_all()
        db.create_all()

        print "Dropped and Created Table.....done"

    def commit(self):
        db.session.commit()
        print "Commited new times"

model_thing = Database_actions()

    # def query(self, bus, stop):
    #     '''Filter by the requested bus and stop and order the times'''
    #     time_list = Mymodel.query.filter(bus=bus and stop=stop).all().order_by(Mymodel.times)
    #     return time_list




if __name__ == "__main__":
    app.run(debug=True)

# an Engine, which the Session will use for connection
# resources
# class Databasestuff(object):
#     def writerow(self, bus, stop, times):
#         some_engine = create_engine('postgressql://khole:databa5318@localhost/busdb')
#
#         # create a configured "Session" class
#         Session = sessionmaker(bind=some_engine)
#
#         # create a Session
#         session = Session()
#
#         # work with sess
