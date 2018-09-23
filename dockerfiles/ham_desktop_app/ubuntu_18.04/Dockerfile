FROM pwsat2/gnu_radio:ubuntu_18.04

MAINTAINER PW-Sat2 Team <kontakt@pw-sat.pl>

USER pwsat2
WORKDIR /home/pwsat2

ARG GIT_REF_GR_KISS="master"

ARG GIT_REF_HIDAPI="a6a622ffb680c55da0de787ff93b80280498330f"
ARG GIT_REF_RTL_SDR="tags/0.6.0"
ARG GIT_REF_GR_FCDPROPLUS="tags/v3.7.12"
ARG GIT_REF_GR_OSMOSDR="4d83c6067f059b0c5015c3f59f8117bbd361e877"

ARG GIT_REF_GR_GPREDICT_DOPPLER="master"

# Install kiss and gr-kiss (KISS and AX.25 blocks for GNU Radio)
RUN pip install kiss && \
    cd /home/pwsat2/GitHub && \
    git clone https://github.com/PW-Sat2/gr-kiss.git && \
    cd gr-kiss && \
    git checkout ${GIT_REF_GR_KISS} && \
    mkdir build && \
    cd build && \
    cmake -DCMAKE_INSTALL_PREFIX=/home/pwsat2/prefix/default .. && \
    make && \
    sudo make install

# Install PlutoSDR
RUN sudo pybombs install gr-iio

# Install FUNCube Dongle Pro+ and RTL-SDR
RUN sudo apt-get update && sudo apt-get install -y libusb-1.0-0-dev libudev-dev && \
    cd /home/pwsat2/GitHub && \
    git clone https://github.com/signal11/hidapi.git && \
    cd hidapi && \
    git checkout ${GIT_REF_HIDAPI} && \
    ./bootstrap && \
    ./configure && \
    make && \
    sudo make install
RUN cd /home/pwsat2/GitHub && \
    git clone https://github.com/osmocom/rtl-sdr.git && \
    cd rtl-sdr/ && \
    git checkout ${GIT_REF_RTL_SDR} && \
    mkdir build && \
    cd build && \
    sudo cmake -DCMAKE_INSTALL_PREFIX=/home/pwsat2/prefix/default .. -DDETACH_KERNEL_DRIVER=ON && \
    sudo make && \
    sudo make install
RUN cd /home/pwsat2/GitHub && \
    git clone https://github.com/dl1ksv/gr-fcdproplus.git && \
    cd gr-fcdproplus && \
    git checkout ${GIT_REF_GR_FCDPROPLUS} && \
    mkdir build && \
    cd build && \
    sudo cmake -DCMAKE_INSTALL_PREFIX=/home/pwsat2/prefix/default .. && \
    sudo make && \
    sudo make install
RUN cd /home/pwsat2/GitHub && \
    git clone https://github.com/osmocom/gr-osmosdr.git && \
    cd gr-osmosdr && \
    git checkout ${GIT_REF_GR_OSMOSDR} && \
    mkdir build && \
    cd build && \
    sudo cmake -DCMAKE_INSTALL_PREFIX=/home/pwsat2/prefix/default .. && \
    sudo make && \
    sudo make install && \
    sudo ldconfig

# Install gr-gpredict-doppler
RUN cd /home/pwsat2/GitHub && \
    git clone https://github.com/PW-Sat2/gr-gpredict-doppler.git && \
    cd gr-gpredict-doppler && \
    git checkout ${GIT_REF_GR_GPREDICT_DOPPLER} && \
    mkdir build && \
    cd build && \
    sudo cmake -DCMAKE_INSTALL_PREFIX=/home/pwsat2/prefix/default .. && \
    sudo make && \
    sudo make install

# Additional packages for the HAM desktop app
RUN sudo pip install pyinstaller colorlog retrying dis3 && \
    sudo apt-get install -y zip
