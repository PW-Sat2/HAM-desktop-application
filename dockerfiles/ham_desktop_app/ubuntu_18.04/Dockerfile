FROM pwsat2/gnu_radio:ubuntu_18.04

MAINTAINER PW-Sat2 Team <kontakt@pw-sat.pl>

USER pwsat2
WORKDIR /home/pwsat2

# Install kiss and gr-kiss (KISS and AX.25 blocks for GNU Radio)
RUN pip install kiss && \
    cd /home/pwsat2/GitHub && \
    git clone https://github.com/PW-Sat2/gr-kiss.git && \
    cd gr-kiss && \
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
    git clone https://github.com/signal11/hidapi && \
    cd hidapi && \
    git checkout a6a622ffb680c55da0de787ff93b80280498330f && \
    ./bootstrap && \
    ./configure && \
    make && \
    sudo make install
RUN cd /home/pwsat2/GitHub && \
    git clone https://git.osmocom.org/rtl-sdr && \
    cd rtl-sdr/ && \
    git checkout 1f0eafe60445339703903af6d8814ffab7e73784 && \
    mkdir build && \
    cd build && \
    sudo cmake -DCMAKE_INSTALL_PREFIX=/home/pwsat2/prefix/default .. && \
    sudo make && \
    sudo make install
RUN cd /home/pwsat2/GitHub && \
    git clone https://github.com/dl1ksv/gr-fcdproplus.git && \
    cd gr-fcdproplus && \
    git checkout 0006c36320cd7a3bc786dd6f186c94809bf445cc && \
    mkdir build && \
    cd build && \
    sudo cmake -DCMAKE_INSTALL_PREFIX=/home/pwsat2/prefix/default .. && \
    sudo make && \
    sudo make install
RUN cd /home/pwsat2/GitHub && \
    git clone https://git.osmocom.org/gr-osmosdr && \
    cd gr-osmosdr && \
    git checkout 4d83c6067f059b0c5015c3f59f8117bbd361e877 && \
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
    mkdir build && \
    cd build && \
    sudo cmake -DCMAKE_INSTALL_PREFIX=/home/pwsat2/prefix/default .. && \
    sudo make && \
    sudo make install

# Additional packages for the HAM desktop app
RUN sudo pip install pyinstaller colorlog retrying dis3 && \
    sudo apt-get install -y zip
