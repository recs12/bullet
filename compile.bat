:: Set this file for compiling the executable.
:: So it can be added to the user custom theme in solidedge. 
ipyc.exe /main:__main__.py api.py holes.py equivalences.py customs.py ^
Interop.SolidEdge.dll ^
/embed ^
/platform:x64 ^
/standalone ^
/target:exe ^
/win32icon:icon.ico ^
/out:bullet_macro-recs_64x_0-0-9 ^
