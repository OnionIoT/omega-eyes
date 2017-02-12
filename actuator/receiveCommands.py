import os
import json
import paho.mqtt.client as mqtt

import cameraControl



### MAIN PROGRAM ###
# find the directory of the script
dirName = os.path.dirname(os.path.abspath(__file__))
print 'dirName is ' + dirName

# read the config file
with open( '/'.join([dirName, 'config.json']) ) as f:
	config = json.load(f)


## setup mqtt
mqttc = mqtt.Client()
camera = cameraControl.cameraControl(0, 1, 1024)

## define the mqtt callbacks
# when connection is made
def on_connect(client, userdata, flags, rc):
    print("Connection result: " + str(rc))
    # subscribe to topic specified by config file
    mqttc.subscribe(config['topic'], 0)

def on_message(client, userdata, msg):
    if msg.payload:
        print(msg.topic + ":: payload is " + str(msg.payload))
        handleMessage(msg.topic, msg.payload)

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_disconnect(client, userdata, rc):
    print("Disconnected from Server")
## end of mqtt callbacks

## other functions
def handleMessage(topic, payload):
    if topic == config['topic']:
        # split payload contents
        positions = payload.split()
        if len(positions) == 2:
            camera.move(int(positions[0]), int(positions[1]) )
            print "Received positions (%d, %d)"%(int(positions[0]), int(positions[1]))
        else:
            print("Invalid number of arguments received")


## Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_disconnect = on_disconnect
# Connect
mqttc.connect(config['server'], config['port'], 60)


# Continue the network loop
mqttc.loop_forever()
