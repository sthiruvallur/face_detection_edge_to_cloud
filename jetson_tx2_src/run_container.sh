#!/usr/bin/env bash
docker run --name mosquitto_broker --network hw03 -p 1883:1883 --rm -ti mosquitto_broker sh
