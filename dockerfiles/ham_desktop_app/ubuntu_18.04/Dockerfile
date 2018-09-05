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

# Install SDRs
RUN sudo apt-get update && sudo apt-get install -y libusb-1.0-0 && \
    sudo pybombs install gr-iio && \
    cd /home/pwsat2/GitHub && \
    git clone https://git.osmocom.org/gr-osmosdr && \
    cd gr-osmosdr && \
    mkdir build && \
    cd build && \
    sudo cmake -DCMAKE_INSTALL_PREFIX=/home/pwsat2/prefix/default .. && \
    sudo make && \
    sudo make install && \
    sudo ldconfig

# Additional packages for the HAM desktop app
RUN sudo pip install pyinstaller colorlog retrying && \
    sudo apt-get install -y zip
