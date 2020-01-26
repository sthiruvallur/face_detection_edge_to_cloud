#!/usr/bin/env bash
docker run --name persist_msg \
--network hw03 \
--rm -ti \
persist_msg:latest
