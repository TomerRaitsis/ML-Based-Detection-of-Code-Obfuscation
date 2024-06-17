
set __VSCMD_script_err_count=0
if "%VSCMD_TEST%" NEQ "" goto :test
if "%VSCMD_ARG_CLEAN_ENV%" NEQ "" goto :clean_env

@REM ------------------------------------------------------------------------
:start

set "PATH=%VSINSTALLDIR%Team Tools\DiagnosticsHub\Collector;%PATH%"

goto :end

@REM ------------------------------------------------------------------------
:test

@REM Test whether VSInstr.exe is now on PATH
where VSInstr.exe > nul 2>&1
if "%ERRORLEVEL%" NEQ "0" (
    @echo [ERROR:%~nx0] 'VSInstr.exe' failed
    set /A __VSCMD_script_err_count=__VSCMD_script_err_count+1
)

goto :end

@REM ------------------------------------------------------------------------
:clean_env

@REM Script only adds to PATH.  No custom action required for -clean_env.
@REM vsdevcmd.bat will clean-up this variable.

goto :end

@REM ------------------------------------------------------------------------
:end

@REM return value other than 0 if tests failed.
if "%__VSCMD_script_err_count%" NEQ "0" (
   set __VSCMD_script_err_count=
   exit /B 1
)

set __VSCMD_script_err_count=
exit /B 0
