@echo off
setlocal
set PROJECT_NAME=ts_lib
set INC_PATH=-I"./h"
set GXX64="C:\Program Files (x86)\TOSUN\TSMaster\Data\Compilers\llvm_mingw_x64\bin\g++.exe"
set GXX32="C:\Program Files (x86)\TOSUN\TSMaster\Data\Compilers\llvm_mingw_x86\bin\g++.exe"

if "%1"=="clean" (
    echo Cleaning dist...
    if exist "dist" rd /s /q "dist"
    exit /b 0
)

if not exist "dist" mkdir "dist"

echo Compiling x64 (.mp64)...
%GXX64% -fms-extensions -shared -Wl,--kill-at %INC_PATH% *.cpp -o "dist/%PROJECT_NAME%.mp64"
if %errorlevel% neq 0 ( echo x64 Failed! && exit /b %errorlevel% )

echo Compiling x86 (.mp)...
%GXX32% -fms-extensions -shared -Wl,--kill-at %INC_PATH% *.cpp -o "dist/%PROJECT_NAME%.mp"
if %errorlevel% neq 0 ( echo x86 Failed! && exit /b %errorlevel% )

echo All builds successful!
echo Output Directory: %~dp0dist
for %%i in (dist\*) do echo %%~ti    %%~nxi
