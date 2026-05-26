@echo off
setlocal
cd /d "%~dp0"

where python >nul 2>nul
if %errorlevel%==0 (
    python app.py
    goto :done
)

where py >nul 2>nul
if %errorlevel%==0 (
    py app.py
    goto :done
)

set "BUNDLED_PYTHON=%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
if exist "%BUNDLED_PYTHON%" (
    "%BUNDLED_PYTHON%" app.py
    goto :done
)

echo Python was not found. Install Python from https://www.python.org/downloads/ and try again.
pause

:done
endlocal
