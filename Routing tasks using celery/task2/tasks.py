from __future__ import absolute_import, unicode_literals
import time

from celery import shared_task


@shared_task#(queue='queue1')
def mul(x, y):
    print("The result is :",x*y)
    time.sleep(10)