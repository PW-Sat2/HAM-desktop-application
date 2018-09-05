Docker containers for [PW-Sat2 HAM Desktop Application](https://github.com/PW-Sat2/HAM-desktop-application). See [PW-Sat2 organization](https://hub.docker.com/u/pwsat2/) at Docker Hub.
It's dedicated to HAM amateur radios allowing for frames collection from [PW-Sat2 satellite](https://pw-sat.pl) and upload to webapp.

# How it works
Docker containters are used to build and test [PW-Sat2 HAM Desktop Application](https://github.com/PW-Sat2/HAM-desktop-application). There are few base images splitted into two main groups:
* `gnu_radio` - base images for various Linux distributions with pre-installed [GNU Radio Companion](https://www.gnuradio.org) via pybombs.
* `ham_desktop_app` - base images for various Linux distributions to build and test [PW-Sat2 HAM Desktop Application](https://github.com/PW-Sat2/HAM-desktop-application). It's based on `gnu_radio` images.

It has been divided into two groups of images because building the GNU Radio Companion takes a long time (few hours).

# How to build docker containers
Install Docker on your host machine:
* [How to Install and Use Docker on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04)

Clone this repository and go to this location. First, you have to build a `gnu_radio` docker image. Select your target distribution, for example go to 
```
[path-to-cloned-git-repo]/dockerfiles/gnu_radio/ubuntu_18.04
```
Then call (this step will take few hours):
```
chmod +x build-docker-image.sh
. ./build-docker-image.sh
```
Assign a tag and push this image into a docker repository:
```
sudo docker login
sudo docker tag gnu_radio pwsat2/gnu_radio:ubuntu_18.04
sudo docker push pwsat2/gnu_radio:ubuntu_18.04
```
Then go to:
```
[path-to-cloned-git-repo]/dockerfiles/ham_desktop_app/ubuntu_18.04
```
And call:
```
chmod +x build-docker-image.sh
. ./build-docker-image.sh
```
Assign a tag and push this image into a docker repository:
```
sudo docker login
sudo docker tag ham_desktop_app pwsat2/ham_desktop_app:ubuntu_18.04
sudo docker push pwsat2/ham_desktop_app:ubuntu_18.04
```

# Useful commands
To run a docker image into bash console, type:
```
sudo docker run -it pwsat2/ham_desktop_app:ubuntu_18.04 /bin/bash
```
For locally prepared images try this way:
```
sudo docker run -it ham_desktop_app /bin/bash
```
