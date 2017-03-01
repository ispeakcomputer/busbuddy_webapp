from celery import Celery

app = Celery('tasks', backend='ampq' , broker='ampq://')
