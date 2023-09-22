@echo off

Set "VIRTUAL_ENV=project_env"

echo [*] Checking for Virtual Environment...

If Not Exist "%VIRTUAL_ENV%\Scripts\activate.bat" (
    echo [*] Virtual Environment not found, setting up project environment...
    pip install virtualenv
    python -m venv project_env

    If Not Exist "%VIRTUAL_ENV%\Scripts\activate.bat" (
        echo [-] An issue with environment setup occurred.
        echo .
        echo [-] Unable to setup Virtual Environment.
        Exit /B 1
    )

    echo [+] Virtual Environment: "%VIRTUAL_ENV%" setup complete.
) else (
    echo [+] Virtual Environment: "%VIRTUAL_ENV%" found.
)

echo [*] Setting "%VIRTUAL_ENV%" as active environment.
Call "%VIRTUAL_ENV%\Scripts\activate.bat"

if %ERRORLEVEL% NEQ 0 (
    echo [-] An issue activating  packages has occurred.
    echo [-] Unable to finish setup.
    Exit /B 1
)

echo [*] Installing packages...
Call pip install openllm & pip install "openllm[llama]"

if %ERRORLEVEL% NEQ 0 (
    echo [-] An issue installing packages has occurred.
    echo [-] Unable to finish setup.
    Exit /B 1
)

echo [+] Packages Installed successfully.
echo [*] Use "%VIRTUAL_ENV%/Scripts/openllm -v" to check version information