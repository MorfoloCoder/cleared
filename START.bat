@echo off

echo starting...

pip install requests pystyle google faker qrcode whois

if %ERRORLEVEL% NEQ 0 (
    echo Failed to install some packages. Exiting.
    exit /b %ERRORLEVEL%
)


python SWIXZ.py

pause
