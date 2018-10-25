set HOME=%USERPROFILE%
set GRCPYTHON="C:\Program Files\GNURadio-3.7\gr-python27\python.exe"
set GRCC="C:\Program Files\GNURadio-3.7\bin\grcc.py"
set PYINSTALLER_GRC="C:\Program Files\GNURadio-3.7\gr-python27\Scripts\pyinstaller.exe"
set GSCONTROL_REPO=D:\Documents\GitHub\GSControl
set HAM_DESKTOP_REPO=D:\Documents\GitHub\HAM-desktop-application

echo "Clean grc part"
cd %HAM_DESKTOP_REPO%\grc_part
rmdir /s /q dist
rmdir /s /q build
rmdir /s /q "%HAM_DESKTOP_REPO%\grc_windows\"
echo "Done"

echo "Generate GRC Python files"

echo "Downlink"
%GRCPYTHON% %GRCC% "%GSCONTROL_REPO%\gnuradio\downlink\downlink.grc" -d "%HAM_DESKTOP_REPO%\grc_part\grc"
echo "File source"
%GRCPYTHON% %GRCC% "%GSCONTROL_REPO%\gnuradio\downlink\source\file_source_path.grc" -d "%HAM_DESKTOP_REPO%\grc_part\grc\source\file_source"
echo "RTL SDR surce"
%GRCPYTHON% %GRCC% "%GSCONTROL_REPO%\gnuradio\downlink\source\rtl_sdr_source_source_parameter.grc" -d "%HAM_DESKTOP_REPO%\grc_part\grc\source\rtl_sdr_source"
echo "SSB source"
%GRCPYTHON% %GRCC% "%GSCONTROL_REPO%\gnuradio\downlink\source\ssb_audio_source_params.grc" -d "%HAM_DESKTOP_REPO%\grc_part\grc\source\ssb_audio_source"


echo "Packing grc_part"
cd %HAM_DESKTOP_REPO%\grc_part
%PYINSTALLER_GRC% grc_part_windows.spec
echo "GRC packed"
cd ..

echo "Copy to grc_windows"
mkdir "%HAM_DESKTOP_REPO%\grc_windows"
xcopy /E "%HAM_DESKTOP_REPO%\grc_part\dist\grc_part" "%HAM_DESKTOP_REPO%\grc_windows"
