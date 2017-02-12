import os
import json
import paho.mqtt.client as mqtt




### MAIN PROGRAM ###
# find the directory of the script
dirName = os.path.dirname(os.path.abspath(__file__))
print 'dirName is ' + dirName

# read the config file
with open( '/'.join([dirName, 'config.json']) ) as f:
	config = json.load(f)


## setup mqtt
mqttc = mqtt.Client()

## define the mqtt callback
# when connection is made
def on_connect(client, userdata, flags, rc):
    print("Connection result: " + str(rc))
    # subscribe to topic specified by config file
    mqttc.subscribe(config['topic'], 0)

def on_message(client, userdata, msg):
    if msg.payload:
        print(msg.topic + ":: payload is " + str(msg.payload))
        #if msg.topic == config['topic']:
        #    handle


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_disconnect(client, userdata, rc):
    print("Disconnected from Server")


## Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_disconnect = on_disconnect
# Connect
mqttc.connect(config['server'], config['port'], 60)


# Continue the network loop
mqttc.loop_forever()
