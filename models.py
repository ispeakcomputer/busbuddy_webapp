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
    times = db.Column(db.Integer)

    def __init__(self,id, bus, stop, times ):
        '''now load model stuff into objects that you can play with'''
        self.bus = bus
        self.stop = stop
        self.times = times
    #
    # def add(self, new_entry):
    #     ''' Load the row into the database '''
    #
    #     self.new_entry = new_entry
    #     print "Going into database"
    #     print new_entry.bus
    #     print new_entry.stop
    #     print new_entry.times
    #
    #     session.add(new_entry)
    #     session.commit()

    # def query(self, bus, stop):
    #     '''Filter by the requested bus and stop and order the times'''
    #     time_list = Mymodel.query.filter(bus=bus and stop=stop).all().order_by(Mymodel.times)
    #     return time_list

    def __repr__(self):
        return '<Bus %r><Stop %r><Times %r>' %self.bus %self.stop %self.times

# if __name__ == "__main__":

    # db.create_all()
    #
    # new_row = Mymodel(bus=str(i), stop='12345'+str(i) , times=str(i)+'12345' )
    # db.session.add(new_row)
    # db.session.commit()

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
