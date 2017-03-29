import os

from django.db.models.signals import pre_delete
from django.dispatch import receiver
from teach.settings import *
from youtube.models import Bloger


@receiver(pre_delete, sender=Bloger)
def bloger_del_img(sender, **kwargs):
    if str(kwargs['instance'].img) == 'bloger/tmp.jpg':
        return

    try:
        os.remove(MEDIA_ROOT + '/' + str(kwargs['instance'].img))
    except Exception:
        pass
    print(str(kwargs['instance'].img))