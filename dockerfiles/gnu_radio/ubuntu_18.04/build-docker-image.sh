#!/bin/bash

sudo docker build -t gnu_radio . |& tee -a ./build-gnu-radio.log
sudo docker images
