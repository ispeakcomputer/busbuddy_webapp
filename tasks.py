from celery import Celery
from backend import *

app = Celery('tasks', broker='ampq://localhost//')

# @app.task(ignore_result=True)

@app.task

def reverser(string):
    return string[::-1]
# def db_reloader():
#     while True:
#         data.pull()
#         feed.get_packaged_data()
#         time.sleep(240)
