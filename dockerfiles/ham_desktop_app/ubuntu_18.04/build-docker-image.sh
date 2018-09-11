#!/bin/bash

sudo docker build --no-cache -t ham_desktop_app . |& tee -a ./build_ham_desktop_app.log
sudo docker images
