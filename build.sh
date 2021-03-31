#!/bin/bash

if [ -z "$1" ]; then
    echo "No image tag provided"
    exit 1
fi

docker build . -t cristianc/paperless-bot:$1
docker push cristianc/paperless-bot:$1
