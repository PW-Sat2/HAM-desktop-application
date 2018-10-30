set GSCONTROL_REPO=D:\Documents\GitHub\GSControl
set HAM_DESKTOP_REPO=D:\Documents\GitHub\HAM-desktop-application
set RELATIVE="C:\Program Files (x86)\Relative\Relative.exe"

echo "Clean main app"
cd %HAM_DESKTOP_REPO%
rmdir /s /q dist
rmdir /s /q build
rmdir /s /q pw-sat-gs-windows
echo "Done"

echo "Build main app"
cd %HAM_DESKTOP_REPO%
pyinstaller main_windows.spec
echo "Done"

echo "Create symlinks"
cd "%HAM_DESKTOP_REPO%\dist"

%RELATIVE% .\main\logs logs
%RELATIVE% .\main\saved_frames saved_frames

cd "%HAM_DESKTOP_REPO%\clean_configs"
xcopy /E /b Run_PW-Sat2_Ground_Station.vbs "%HAM_DESKTOP_REPO%\dist"

echo "Copy to pw-sat-gs-windows"
mkdir "%HAM_DESKTOP_REPO%\pw-sat-gs-windows"
xcopy /E /b "%HAM_DESKTOP_REPO%\dist" "%HAM_DESKTOP_REPO%\pw-sat-gs-windows"
cd ..
