#!/usr/bin/env python
import Adafruit_DHT


class Sensor:
    def __init__(self, sensor=Adafruit_DHT.DHT22, pin=4):
        self.SENSOR = sensor
        self.PIN = pin
        self.humidity, self.temperature = Adafruit_DHT.read_retry(self.SENSOR, self.PIN)

    def getTemperature(self):
        return self.temperature

    def getHumidity(self):
        return self.humidity

    def getSENSOR(self):
        return self.SENSOR

    def getPIN(self):
        return self.PIN

    def setSENSOR(self, sensor):
        sensor_args = { '11': Adafruit_DHT.DHT11,
                        '22': Adafruit_DHT.DHT22,
                        '2302': Adafruit_DHT.AM2302 }
        self.SENSOR = sensor_args[sensor]

    def setPIN(self, pin):
        self.PIN = pin

    def refresh(self):
        self.humidity, self.temperature = Adafruit_DHT.read_retry(self.SENSOR, self.PIN)
