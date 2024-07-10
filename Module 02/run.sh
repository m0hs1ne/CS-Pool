#!/bin/bash

DOCKER_IMAGE_NAME="tor-nginx"
CONTAINER_NAME="tor-web"

echo "Building Docker image..."
docker build -t $DOCKER_IMAGE_NAME .

if [ $? -ne 0 ]; then
    echo "Docker build failed. Exiting."
    exit 1
fi

if [ "$(docker ps -aq -f name=^/${CONTAINER_NAME}$)" ]; then
    echo "Container already exists. Removing it..."
    docker rm -f $CONTAINER_NAME
fi

echo "Running Docker container..."
docker run -d --name $CONTAINER_NAME $DOCKER_IMAGE_NAME

echo "Waiting for Tor to generate the hostname (this may take some time)..."
sleep 25

echo "Retrieving .onion hostname..."
ONION_HOSTNAME=$(docker exec -it $CONTAINER_NAME cat /var/lib/tor/ft_onion/hostname)

if [ -z "$ONION_HOSTNAME" ]; then
    echo "Failed to retrieve .onion hostname. Please check the container logs."
else
    echo "Your .onion hostname is: $ONION_HOSTNAME"
fi

echo "You can ssh into the container using the following ip address: $(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $CONTAINER_NAME)"

echo "Setup complete!"