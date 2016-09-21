#!/usr/bin/env python
import peewee
from peewee import *

DATABASE = 'dht22'
database = MySQLDatabase(DATABASE, user='root', passwd='root')


class BaseModel(peewee.Model):
    class Meta:
        database = database


class Measurements(peewee.Model):
    id = IntegerField(unique=True)
    timestamp = DateTimeField(
        constraints=[SQL("DEFAULT (datetime('now'))")])
    temp = DoubleField()
    humidity = DoubleField()

    class Meta:
        order_by = ('id',)
