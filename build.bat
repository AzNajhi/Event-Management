@echo off
pyinstaller --onefile --noconsole ^
   --icon "Event Management System\Icon\Mezza9-Icon.ico" ^
   --hidden-import options ^
   --hidden-import automated ^
   --hidden-import manual ^
   --hidden-import autotable ^
   --hidden-import manualtable ^
   --hidden-import autosave ^
   --hidden-import manualsave ^
   "Event Management System\main.py"

del /q main.spec
rmdir /s /q build
rmdir /s /q "Executable File"
ren dist "Executable File"
xcopy "Event Management System\Icon" "Executable File\Icon" /e /i /s
tar -a -c -f "Executable File.zip" "Executable File"
rmdir /s /q "Executable File"