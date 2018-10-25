#!/bin/bash

source config.sh

echo "Cleaning..."

echo "GSControl clean"
rm -r $path_to_ham_desktop_application/grc_part/dist
echo "GSControl clean done"

echo "HAM-desktop-application clean"
rm -r $path_to_ham_desktop_application/pw-sat2-gs
rm -r $path_to_ham_desktop_application/grc_linux/*
echo "HAM-desktop-application clean done"

echo "build clean"
rm -r $path_to_ham_desktop_application/pw-sat2-gs.zip

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
grcc funcube_source_source_parameter.grc -d $path_to_ham_desktop_application/grc_part/grc/source/funcube_source

echo "PlutoSDR Source"
cd $path_to_gscontrol/gnuradio/downlink/source
grcc plutosdr_source_source_parameter.grc -d $path_to_ham_desktop_application/grc_part/grc/source/plutosdr_source

echo "RTL SDR surce"
cd $path_to_gscontrol/gnuradio/downlink/source
grcc rtl_sdr_source_source_parameter.grc -d $path_to_ham_desktop_application/grc_part/grc/source/rtl_sdr_source

echo "SSB audio surce"
cd $path_to_gscontrol/gnuradio/downlink/source
grcc ssb_audio_source_params.grc -d $path_to_ham_desktop_application/grc_part/grc/source/ssb_audio_source

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

echo "Remove problematic libraries..."

rm -r $path_to_ham_desktop_application/dist/main/libglib-2.0.so.0
rm -r $path_to_ham_desktop_application/dist/main/grc_linux/libglib-2.0.so.0

rm -r $path_to_ham_desktop_application/dist/main/libgio-2.0.so.0

rm -r $path_to_ham_desktop_application/dist/main/libstdc++.so.6
rm -r $path_to_ham_desktop_application/dist/main/grc_linux/libstdc++.so.6

rm -r $path_to_ham_desktop_application/dist/main/libz.so.1
rm -r $path_to_ham_desktop_application/dist/main/grc_linux/libz.so.1

rm -r $path_to_ham_desktop_application/dist/main/libfreetype.so.6
rm -r $path_to_ham_desktop_application/dist/main/grc_linux/libfreetype.so.6

rm -r $path_to_ham_desktop_application/dist/main/libfontconfig.so.1
rm -r $path_to_ham_desktop_application/dist/main/grc_linux/libfontconfig.so.1

echo "Finished"

echo "Create symlinks"
cd $path_to_ham_desktop_application/dist
ln -rs $path_to_ham_desktop_application/dist/main/main PW-Sat2_Ground_Station
ln -rs $path_to_ham_desktop_application/dist/main/logs logs
ln -rs $path_to_ham_desktop_application/dist/main/saved_frames saved_frames

echo "Rename and Compress"
mv $path_to_ham_desktop_application/dist $path_to_ham_desktop_application/pw-sat2-gs

cd $path_to_ham_desktop_application
zip --symlinks -r pw-sat2-gs pw-sat2-gs

echo "Done"





