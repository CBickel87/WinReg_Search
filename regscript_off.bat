FOR /F "delims=" %%i IN (complist.txt) DO (
 sc \\%%i stop remoteregistry
)

pause
