#!/bin/bash

sudo docker build -t ham_desktop_app . |& tee -a ./build_ham_desktop_app.log
sudo docker images
