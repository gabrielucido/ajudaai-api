#!/bin/bash

apt-get update
apt-get -y install libpq-dev python-dev gcc netcat make cron

if [ "$MODE" = "production" ]; then
    pip install -r prod.txt
else
    pip install -r dev.txt
fi
