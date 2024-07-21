#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
docker pull navyab/python-flask-app

# Run the Docker image as a container
docker run -d -p 5000:5000 navyab/python-flask-app