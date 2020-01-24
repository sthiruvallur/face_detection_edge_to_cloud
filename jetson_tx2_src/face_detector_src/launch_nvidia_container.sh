#!/usr/bin/env bash

xhost +
sudo docker run -it --rm --net=host --network hw03 --privileged --runtime nvidia  -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix -v"$PWD":/HW3  face_detect_cntr:latest
