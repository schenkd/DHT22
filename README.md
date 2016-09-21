# DHT22
python script for my dht22 sensor

## coming soon
- [X] Sensor class
- [X] ORM with peewee
- [ ] failure log

## database
In this project I'm using a new ORM lib called peewee.

It's lighter than SQLAlchemy.

### Setup

Install packages
```batch
sudo apt-get install mysql-server mysql-client php5-mysql libmysqlclient-dev
```

```batch
pip install MySQL-python peewee
```

Now you can import the peewee lib in your python project.

## How can I use my sensor on a raspberry pi?

### Hardware

I'm using a Type: Pi 2, Revision: 01, Memory: 1024MB, Maker: Sony and a 100k Ohm resistor.


Breadboard connection:

![alt text](http://www.knight-of-pi.org/wp-content/uploads/2015/03/breadboard_dht22.jpg "RPi")


## Software

Install packages
```batch
sudo apt-get install build-essential python-dev python-openssl git
```

Get Adafruit lib from github
```batch
git clone https://github.com/adafruit/Adafruit_Python_DHT.git && cd Adafruit_Python_DHT
sudo python setup.py install
```

Test your sensor
```batch
cd examples
sudo ./AdafruitDHT.py 22 4
```
