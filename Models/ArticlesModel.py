# -*- coding: utf-8 -*-

from Mapping.models import Articles
from bson.objectid import ObjectId
import time

def list():
    return 'xx'

def show(id):
    return 'xx'

def add(param):

    dataObject = Articles.objects.create(
        id=ObjectId(),
        title='xxxxxxxxxxxxxtitle',
        desc='xxxxxxxxxxxxxxxdesc',
        create=int(time.time()),
        uid=ObjectId('58feeb99fbd43e76c88f40bd')
    )

    id = dataObject.id
    dataObject.save()

    return id