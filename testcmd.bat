@echo off
for /f "delims=" %%i in (laiyue_target_file.txt) do (
	md %2\%%i
	xcopy /y /s /i %1\%%i %2\%%i
)

pause