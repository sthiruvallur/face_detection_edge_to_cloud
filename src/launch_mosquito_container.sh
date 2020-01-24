#!/usr/bin/env bash

echo "I am going to create a network bridge now"

# Create a bridge:
docker network create --driver bridge hw03

# Create an alpine linux - based mosquitto container:
docker run --name mosquitto --network hw03 -p 1883:1883 -ti alpine sh

