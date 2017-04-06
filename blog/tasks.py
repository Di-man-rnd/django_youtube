# -*- coding: utf-8 -*-
from celery.task import task


@task()
def just_print():
    print( "Print from celery task")