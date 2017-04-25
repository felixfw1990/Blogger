# -*- coding: utf-8 -*-
from Mapping.models import Articles
from bson.objectid import ObjectId
import time

def articles():
    list = Articles.objects
    return list

def show(id):
    return 'xx'

def add(param):

    _id = ObjectId()
    Articles.objects.create(
        _id=_id,
        title='xxxxxxxxxxxxxtitle',
        desc='xxxxxxxxxxxxxxxdesc',
        create=int(time.time()),
        uid=ObjectId('58feeb99fbd43e76c88f40bd')
    )

    return _id