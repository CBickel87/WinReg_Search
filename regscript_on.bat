FOR /F "delims=" %%i IN (complist.txt) DO (
 sc \\%%i start remoteregistry
)

pause
