@echo off

Set "VIRTUAL_ENV=.project_env"

echo [*] Setting up Server project...

cd server

echo [*] Checking for Virtual Environment. & echo:

If Not Exist "%VIRTUAL_ENV%\Scripts\activate.bat" (
    echo [*] Virtual Environment not found, setting up project environment...
    pip install virtualenv
    python -m venv %VIRTUAL_ENV%

    If Not Exist "%VIRTUAL_ENV%\Scripts\activate.bat" (
        echo [-] An issue with environment setup occurred.
        echo [-] Unable to setup Virtual Environment.
        Exit /B 1
    )

    echo [+] Virtual Environment: "%VIRTUAL_ENV%" setup complete.
) else (
    echo [+] Virtual Environment: "%VIRTUAL_ENV%" found. & echo:
)

echo [*] Setting "%VIRTUAL_ENV%" as active environment.
Call "%VIRTUAL_ENV%\Scripts\activate.bat"

if %ERRORLEVEL% NEQ 0 (
    echo [-] An issue activating environment has occurred.
    echo [-] Unable to finish setup.
    Exit /B 1
)

echo [*] Installing packages...

@Rem This brings in these 2 modules and all their dependencies
Call pip install django & pip install langchain[llms] & pip install google-cloud-aiplatform & pip install anthropic

if %ERRORLEVEL% NEQ 0 (
    echo [-] An issue installing packages has occurred.
    echo [-] Unable to finish setup.
    Exit /B 1
)

echo [+] Packages Installed successfully.
echo [+] Server files installed. & echo:

echo [+] Finished server project setup...

cd ../client

echo [*] Setting up client app...
Call "npm install"

@REM Put setup for front end and React setup here...
echo [+] Packages Installed successfully.
echo [+] Client files installed.