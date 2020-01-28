#!/usr/bin/env bash
sudo s3fs w251-homework3 /mnt/w251-homework3 -o nonempty  -o passwd_file=$HOME/.cos_creds -o sigv2 -o use_path_request_style -o url=https://s3.us-east.objectstorage.softlayer.net
docker run --name persist_msg \
--network hw03 \
--rm -ti \
-v /mnt/w251-homework3:/mnt/w251-homework3:rw \
persist_msg:latest
