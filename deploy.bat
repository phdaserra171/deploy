@echo off
cd /d "C:\Users\PC\Desktop\brada\deploy"
set PATH=%PATH%;"C:\Program Files\nodejs"
for /f "delims=" %%i in ('npm config get prefix') do set NPM_PREFIX=%%i
"%NPM_PREFIX%\surge.cmd" --help