#!/bin/bash

DOCKER_IMAGE_NAME="tor-nginx"
CONTAINER_NAME="tor-web"

docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME
docker rmi $DOCKER_IMAGE_NAME

echo "Cleanup complete. Container and image removed."