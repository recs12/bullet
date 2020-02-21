:: Set this file for compiling the executable.
:: So it can be added to the user custom theme in solidedge. 
ipyc.exe /main:./bullet/__main__.py ./bullet/Interop.SolidEdge.dll ./bullet/api.py ./bullet/holes.py ./bullet/equivalences.py ./bullet/customs.py ^
/embed ^
/out:bullet_macro-recs_64x_0-0-7 ^
/platform:x64 ^
/standalone ^
/target:exe ^
/win32icon:bullet.ico 
