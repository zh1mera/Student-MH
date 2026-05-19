@echo off
title HealthSync Server

:: Set the current directory to the folder where this .bat file is located
cd /d "%~dp0"

echo ========================================================
echo       HealthSync: Student Mental Health System
echo ========================================================
echo.
echo Installing/Verifying required AI libraries...
echo (This may take a moment on the first run)
python -m pip install -r requirements.txt --quiet
echo.
echo Starting the Artificial Intelligence modules...
echo Starting the Flask Web Server...
echo.
echo Your browser will open automatically in a few seconds.
echo If it doesn't, please go to: http://127.0.0.1:5000
echo.

:: Wait for 2 seconds (removed the NUL redirection to prevent errors on some devices)
timeout /t 2 /nobreak

:: Open the web browser
start http://127.0.0.1:5000

:: Start the python flask server
python app.py

pause
