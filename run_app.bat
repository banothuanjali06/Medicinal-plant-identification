@echo off
echo.
echo ========================================
echo   🌿 Medicinal Plant Identifier App
echo ========================================
echo   Starting the application...
echo   Powered by Google Gemini AI
echo ========================================
echo.

cd /d "c:\myfiles chintu\new projects ai peters\MEDICINAL PLANTS IDENTIFICATION AND USES"

echo Installing/Checking dependencies...
pip install -r requirements.txt

echo.
echo Starting Gradio app...
echo.
python medicinal_plant_app.py

echo.
echo App has stopped. Press any key to exit...
pause