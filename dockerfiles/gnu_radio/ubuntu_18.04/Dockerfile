FROM ubuntu:18.04

MAINTAINER PW-Sat2 Team <kontakt@pw-sat.pl>

RUN  apt-get update && apt-get install -y sudo git python-pip

RUN useradd --create-home --shell /bin/bash pwsat2 && \
    passwd --delete pwsat2 && \
    adduser pwsat2 sudo

USER pwsat2
WORKDIR /home/pwsat2

RUN mkdir /home/pwsat2/GitHub && \
    cd /home/pwsat2/GitHub && \
    git clone https://github.com/gnuradio/pybombs.git && \
    cd pybombs && \
    sudo python setup.py install && \
    pybombs recipes add gr-recipes git+https://github.com/gnuradio/gr-recipes.git && \
    pybombs recipes add gr-etcetera git+https://github.com/gnuradio/gr-etcetera.git && \
    mkdir /home/pwsat2/prefix && \
    mkdir /home/pwsat2/prefix/default && \
    pybombs prefix init /home/pwsat2/prefix/default/ && \
    sudo pybombs install gnuradio && \
    sudo chmod +x /home/pwsat2/prefix/default/setup_env.sh
