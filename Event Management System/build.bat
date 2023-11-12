@echo off
pyinstaller --onefile ^
   --hidden-import options ^
   --hidden-import automated ^
   --hidden-import manual ^
   --hidden-import autotable ^
   --hidden-import manualtable ^
   --hidden-import autosave ^
   --hidden-import mansave ^
   .\Event Management System\main.py
