:: Set this file for compiling the executable.
:: So it can be added to the user custom theme in solidedge. 
ipyc.exe /main:__main__.ipy 
api.ipy ^
holes.ipy ^
equivalences.ipy ^ 
customs.ipy ^
Interop.SolidEdge.dll ^
/embed ^
/out:bullet_macro-recs_64x_0-0-9 ^
/platform:x64 ^
/standalone ^
/target:exe ^
/win32icon:bullet.ico 
