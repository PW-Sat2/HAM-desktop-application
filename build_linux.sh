#!/bin/bash

source config.sh

echo "Cleaning..."

echo "GSControl clean"
rm -r $path_to_ham_desktop_application/grc_part/dist
echo "GSControl clean done"

echo "HAM-desktop-application clean"
rm -r $path_to_ham_desktop_application/dist
rm -r $path_to_ham_desktop_application/grc_linux/*
echo "HAM-desktop-application clean done"

echo "Setup GRC env"
source $path_to_gr_env/setup_env.sh


echo "Generate GRC Python files"

echo "Downlink"
cd $path_to_gscontrol/gnuradio/downlink
grcc downlink.grc -d $path_to_ham_desktop_application/grc_part/grc

echo "File source"
cd $path_to_gscontrol/gnuradio/downlink/source
grcc file_source_path.grc -d $path_to_ham_desktop_application/grc_part/grc/source/file_source

echo "Funcube source"
cd $path_to_gscontrol/gnuradio/downlink/source
grcc funcube_source.grc -d $path_to_ham_desktop_application/grc_part/grc/source/funcube_source

echo "PlutoSDR Source"
cd $path_to_gscontrol/gnuradio/downlink/source
grcc plutosdr_source.grc -d $path_to_ham_desktop_application/grc_part/grc/source/plutosdr_source

echo "RTL SDR surce"
cd $path_to_gscontrol/gnuradio/downlink/source
grcc rtl_sdr_source.grc -d $path_to_ham_desktop_application/grc_part/grc/source/rtl_sdr_source

echo "Packing grc_part"
cd $path_to_ham_desktop_application/grc_part
pyinstaller grc_part_linux.spec
echo "GRC packed"

echo "Copy grc_part"
mkdir $path_to_ham_desktop_application/grc_linux
cp -r $path_to_ham_desktop_application/grc_part/dist/grc_part/* $path_to_ham_desktop_application/grc_linux

echo "Packing main app"
cd $path_to_ham_desktop_application
pyinstaller main_linux.spec
echo "Finished"

echo "Run"
cd $path_to_ham_desktop_application/dist/main
./main




