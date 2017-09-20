#!/bin/sh

## script to install python and required modules

opkg update
opkg install python-light pyPwmExp
opkg install python-pip
pip install --upgrade setuptools

pip install paho-mqtt

# copy controlle rservice file and start the service
cp etc/init.d/actuator /etc/init.d/actuator
chmod +x /etc/init.d/actuator

/etc/init.d/actuator enable
/etc/init.d/actuator restart