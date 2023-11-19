cd "%1"
cd client

if "%NEXTJS_DEBUG%" == "True" (
    npx next dev -H %NEXTJS_ADDRESS% -p %NEXTJS_PORT%
) else (
    npx next build
    npx next start -H %NEXTJS_ADDRESS% -p %NEXTJS_PORT%
)
pause
