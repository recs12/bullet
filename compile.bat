:: Set this file for compiling the executable.
:: So it can be added to the user custom theme in solidedge. 
ipyc.exe /main:./bullet/__main__.py ./bullet/api.py ./bullet/holes.py ./bullet/equivalences.py ./bullet/customs.py ^
./bullet/Interop.SolidEdge.dll ^
/embed ^
/out:bullet_macro-recs_64x_0-0-9 ^
/platform:x64 ^
/standalone ^
/target:exe ^
/win32icon:bullet.ico 
