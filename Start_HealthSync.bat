@echo off
title HealthSync Server
echo ========================================================
echo       HealthSync: Student Mental Health System
echo ========================================================
echo.
echo Starting the Artificial Intelligence modules...
echo Starting the Flask Web Server...
echo.
echo Your browser will open automatically in a few seconds.
echo If it doesn't, please go to: http://127.0.0.1:5000
echo.

:: Wait for 2 seconds to give the user time to read
timeout /t 2 /nobreak > NUL

:: Open the web browser
start http://127.0.0.1:5000

:: Start the python flask server
python app.py

pause
