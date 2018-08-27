# HAM-desktop-application
Application dedicated to HAM amateur radios allowing for frames collection and upload to webapp.

![image](https://user-images.githubusercontent.com/6267528/44672229-1e62b800-aa28-11e8-8ff3-fef2fa952f2f.png)


## Builds (freezes)
Binaries for supported platforms are available to download on http://radio.pw-sat.pl/communication/desktopsoftware. Binaries contain also freezed GNURadio Companion (GRC) flow graphs. It's strongly recommended to use these binaries.

More help on the operation of application can be found in Wiki: https://github.com/PW-Sat2/HAMRadio/wiki

## More details about architecture

In fact, the software comprises two parts:
  * main application - functions like: showing main window, frames list, receiving frames via ZMQ, having buttons to run external binaries with GRC part: signal sources/SDR, demodulator etc.
  * GnuRadio Companion part - signal source: SDRs, IQ files, demodulator/decoder - always freezed as binary
  
  This repo itself does not contain GRC part - running `main.py` file one can use all functionalities but `Signal source` and `Demodulator`.


## Usage (with your Python interpreter and GnuRadio Companion)

### Main application
Just run `main.py` file via Python 2.6 interpreter.

### GnuRadio part

Run selected flow charts from https://github.com/PW-Sat2/GSControl/tree/master/gnuradio/downlink repository in GnuRadio Companion:
- `downlink.grc` is "Run demodulator" option from main application
- a directory `sources` contains 

Out-of-tree GRC block you can find in a repository https://github.com/PW-Sat2/gr-kiss


## How to build binary

### Linux (tested on Ubuntu 16.04 - 18.04)
1. Install GRC so you can run everything in https://github.com/PW-Sat2/GSControl/tree/master/gnuradio/downlink repository
2. Install all python dependencies so you can run Main application from this repository (try `main.py` file)
3. Clone https://github.com/PW-Sat2/GSControl repository
4. Clone https://github.com/PW-Sat2/HAM-desktop-application repository
5. Adjust non-relative paths in these two files: https://github.com/PW-Sat2/HAM-desktop-application/blob/main-app/main_linux.spec and https://github.com/PW-Sat2/HAM-desktop-application/blob/main-app/grc_part/grc_part_linux.spec
6. Correct paths to GSControl repository and HAM-desktop-application repositories in file https://github.com/PW-Sat2/HAM-desktop-application/blob/main-app/config.sh
7. Run `build_linux.sh` file from this repository. At the end of building process the application should be run.
