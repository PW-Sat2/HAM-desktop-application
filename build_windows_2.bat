set GSCONTROL_REPO=D:\Documents\GitHub\GSControl
set HAM_DESKTOP_REPO=D:\Documents\GitHub\HAM-desktop-application

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

cmd /c mklink PW-Sat2_Ground_Station .\main\main.exe
cmd /c mklink /d logs .\main\logs
cmd /c mklink /d saved_frames .\main\saved_frames

echo "Copy to pw-sat-gs-windows"
mkdir "%HAM_DESKTOP_REPO%\pw-sat-gs-windows"
xcopy /E /b "%HAM_DESKTOP_REPO%\dist" "%HAM_DESKTOP_REPO%\pw-sat-gs-windows"
