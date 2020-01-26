#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import uuid


LOCAL_MQTT_HOST="10.190.17.195"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="persist_faces"

def on_connect_local(client, userdata, flags, rc):
  print("connected to local broker with rc: " + str(rc))
	
def on_message(client,userdata, msg):
  try:
    print("message received!")
    print("Received message of len:{} bytes from topic:{}".format(len(msg.payload), msg.topic) )
    # Publishing this message to the cloud broker
    guid = str(uuid.uuid4())
    msg = msg.payload
    file_path = '/var/data/w251/hw/homework3/images/' + "detect_faces" + guid + ".png"
    with open(file_path, 'wb') as outfile:
      outfile.write(msg)
  except:
    print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)

local_mqttclient.subscribe(LOCAL_MQTT_TOPIC, qos=2)
local_mqttclient.on_message = on_message

# go into a loop
local_mqttclient.loop_forever()
