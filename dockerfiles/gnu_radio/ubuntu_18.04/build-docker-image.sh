#!/bin/bash

sudo docker build --no-cache -t gnu_radio . |& tee -a ./build-gnu-radio.log
sudo docker images
