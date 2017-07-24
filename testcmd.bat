@echo off
for /f "delims=" %%i in (target_file1.txt) do (
	md %2\%%i
	xcopy /y /s /i %1\%%i %2\%%i
)

pause