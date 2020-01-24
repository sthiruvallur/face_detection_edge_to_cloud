#!/usr/bin/env bash

xhost +
sudo docker run -it --rm --net=host --runtime nvidia  -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix -v"$PWD":/HW3  nvcr.io/nvidia/l4t-base:r32.3.1
