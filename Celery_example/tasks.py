from celery import Celery 
from time import sleep

app = Celery('tasks', backend='db+sqlite:///db.sqlite3')

@app.task 
def add(x,y):
    sleep(2)
    return x + y