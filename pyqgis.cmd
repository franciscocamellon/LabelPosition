@echo off
SET OSGEO4W_ROOT=D:\OSGeo4W64
call "%OSGEO4W_ROOT%"\bin\o4w_env.bat

@echo off
PATH %PATH%;%OSGEO4W_ROOT%\apps\qgis\bin
PATH %PATH%;%OSGEO4W_ROOT%\apps\grass\grass78\lib
PATH %PATH%;D:\OSGeo4W64\apps\Qt5\bin
PATH %PATH%;D:\OSGeo4W64\apps\Python37\Scripts

SET PYTHONPATH=%PYTHONPATH%;%OSGEO4W_ROOT%\apps\qgis\python
SET OYTHINHOME=%OSGEO4W_ROOT%\APPS\Pythin37

SET PATH=D:\Program Files\Git\bin;%PATH%

cmd.exe