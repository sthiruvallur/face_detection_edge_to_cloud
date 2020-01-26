#!/usr/bin/env bash
docker run --name mosquitto_broker \
--network hw03 \
-p 1883:1883 \
--rm -tid \
mosquitto_broker
#-v '/media/mosquitto/config:/mqtt/config:ro' \
#-v '/media/mosquitto/data:/mqtt/data' \ 
#-v /media/mosquitto/log:/mqtt/log \ 
