#!/bin/sh

## script to configure joystick controller to install required packages and start publishing to topic

opkg update
opkg install mosquitto-ssl mosquitto-client

/etc/init.d/mosquitto enable
/etc/init.d/mosquitto restart

# copy controlle rservice file and start the service
cp etc/init.d/controller /etc/init.d/controller
chmod +x /etc/init.d/controller

/etc/init.d/controller enable
/etc/init.d/controller restart