#!/bin/bash
docker build -t qr-app .
docker run -p 5000:5000 qr-app
