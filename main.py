#!/usr/bin/env python
from db import database, Measurements
from sensor import *


sensor = Sensor()

try:
    with database.transaction():
        measurement = Measurements.create(
            temp=sensor.getTemperature(),
            humidity=sensor.getHumidity()
        )
except IntegrityError:
    # write error in log soon
    pass
