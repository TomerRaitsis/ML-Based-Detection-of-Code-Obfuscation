@ECHO OFF
SETLOCAL

::----------------------------------------------------------------------
:: Android Studio startup script.
::----------------------------------------------------------------------

:: ---------------------------------------------------------------------
:: Ensure System32 is in PATH.
:: ---------------------------------------------------------------------
SET PATH=%PATH%;%systemroot%\system32

:: ---------------------------------------------------------------------
:: Ensure IDE_HOME points to the directory where the IDE is installed.
:: ---------------------------------------------------------------------
SET IDE_BIN_DIR=%~dp0
FOR /F "delims=" %%i in ("%IDE_BIN_DIR%\..") DO SET IDE_HOME=%%~fi

:: ---------------------------------------------------------------------
:: Locate a JRE installation directory which will be used to run the IDE.
:: Try (in order): STUDIO_JDK, studio%BITS%.exe.jdk, ..\jbr[-x86], JDK_HOME, JAVA_HOME.
:: ---------------------------------------------------------------------
SET JRE=%IDE_HOME%\jbr
SET JAVA_HOME=
SET STUDIO_JDK=
SET JDK_HOME=
SET JAVA_EXE=%JRE%\bin\java.exe
IF NOT EXIST "%JAVA_EXE%" (
  ECHO ERROR: cannot start Android Studio.
  ECHO No JRE found. Please make sure STUDIO_JDK, JDK_HOME, or JAVA_HOME point to a valid JRE installation.
  EXIT /B
)

:: ---------------------------------------------------------------------
:: Collect JVM options and properties.
:: ---------------------------------------------------------------------
IF NOT "%STUDIO_PROPERTIES%" == "" SET IDE_PROPERTIES_PROPERTY="-Didea.properties.file=%STUDIO_PROPERTIES%"

SET VM_OPTIONS_FILE=
SET USER_VM_OPTIONS_FILE=

SET STUDIO_VERSION=
FOR /F "tokens=2 delims= " %%x in ('FINDSTR AndroidStudio "%IDE_HOME%\product-info.json"') do set STUDIO_VERSION=%%x
SET STUDIO_VERSION=%STUDIO_VERSION:"=%
SET STUDIO_VERSION=%STUDIO_VERSION:,=%

SET BITS=64
REG Query "HKLM\Hardware\Description\System\CentralProcessor\0" | FIND /i "x86" > NUL && SET BITS=
SET STUDIO_EXE=%IDE_HOME%\bin\studio%BITS%.exe

SET STUDIO_CONFIG_DIR="%APPDATA%\Google\%STUDIO_VERSION%\%"
IF NOT EXIST %STUDIO_CONFIG_DIR% (
  @REM Android Studio config is not set up
  ECHO Android Studio config doesn't exist %STUDIO_CONFIG_DIR%
  "%STUDIO_EXE%" disableNonBundledPlugins dontReopenProjects
  EXIT /B
)

SET STUDIO_SAFE_CONFIG_DIR="%APPDATA%\Google\%STUDIO_VERSION%.safe\%"
IF NOT EXIST %STUDIO_SAFE_CONFIG_DIR% (
  mkdir %STUDIO_SAFE_CONFIG_DIR%
  EXIT /B
)

xcopy /YS %STUDIO_CONFIG_DIR%* %STUDIO_SAFE_CONFIG_DIR%
del %STUDIO_SAFE_CONFIG_DIR%idea.properties
del %STUDIO_SAFE_CONFIG_DIR%studio64.exe.vmoptions

USER_VM_OPTIONS_FILE=%APPDATA%\Google\%STUDIO_VERSION%.safe\studio64.exe.vmoptions
SET ACC="-Djb.vmOptionsFile=%USER_VM_OPTIONS_FILE%"
FINDSTR /R /C:"-XX:\+.*GC" "%USER_VM_OPTIONS_FILE%" > NUL

SET "CLASS_PATH=%CLASS_PATH%;%IDE_HOME%\lib\util.jar"
SET "CLASS_PATH=%CLASS_PATH%;%IDE_HOME%\lib\externalProcess-rt.jar"
SET "CLASS_PATH=%CLASS_PATH%;%IDE_HOME%\lib\groovy.jar"
SET "CLASS_PATH=%CLASS_PATH%;%IDE_HOME%\lib\external-system-rt.jar"
SET "CLASS_PATH=%CLASS_PATH%;%IDE_HOME%\lib\resources.jar"
SET "CLASS_PATH=%CLASS_PATH%;%IDE_HOME%\lib\lib.jar"
SET "CLASS_PATH=%CLASS_PATH%;%IDE_HOME%\lib\intellij-coverage-agent-1.0.738.jar"
SET "CLASS_PATH=%CLASS_PATH%;%IDE_HOME%\lib\byte-buddy-agent.jar"
SET "CLASS_PATH=%CLASS_PATH%;%IDE_HOME%\lib\jps-model.jar"
SET "CLASS_PATH=%CLASS_PATH%;%IDE_HOME%\lib\ant/lib/ant.jar"
SET "CLASS_PATH=%IDE_HOME%\lib\platform-loader.jar"
SET "CLASS_PATH=%CLASS_PATH%;%IDE_HOME%\lib\forms_rt.jar"
SET "CLASS_PATH=%CLASS_PATH%;%IDE_HOME%\lib\grpc.jar"
SET "CLASS_PATH=%CLASS_PATH%;%IDE_HOME%\lib\util_rt.jar"
SET "CLASS_PATH=%CLASS_PATH%;%IDE_HOME%\lib\bouncy-castle.jar"
SET "CLASS_PATH=%CLASS_PATH%;%IDE_HOME%\lib\idea_rt.jar"
SET "CLASS_PATH=%CLASS_PATH%;%IDE_HOME%\lib\app.jar"
SET "CLASS_PATH=%CLASS_PATH%;%IDE_HOME%\lib\junit4.jar"
SET "CLASS_PATH=%CLASS_PATH%;%IDE_HOME%\lib\util-8.jar"
SET "CLASS_PATH=%CLASS_PATH%;%IDE_HOME%\lib\annotations.jar"
SET "CLASS_PATH=%CLASS_PATH%;%IDE_HOME%\lib\intellij-test-discovery.jar"
SET "CLASS_PATH=%CLASS_PATH%;%IDE_HOME%\lib\error-prone-annotations.jar"
SET "CLASS_PATH=%CLASS_PATH%;%IDE_HOME%\lib\protobuf.jar"
SET "CLASS_PATH=%CLASS_PATH%;%IDE_HOME%\lib\rd.jar"
SET "CLASS_PATH=%CLASS_PATH%;%IDE_HOME%\lib\stats.jar"

:: ---------------------------------------------------------------------
:: Run the IDE.
:: ---------------------------------------------------------------------
"%JAVA_EXE%" ^
  -cp "%CLASS_PATH%" ^
  %ACC% ^
  "-XX:ErrorFile=%USERPROFILE%\java_error_in_studio_%%p.log" ^
  "-XX:HeapDumpPath=%USERPROFILE%\java_error_in_studio.hprof" ^
  %IDE_PROPERTIES_PROPERTY% ^
  -Djava.system.class.loader=com.intellij.util.lang.PathClassLoader -Dstudio.safe.mode=true -Didea.vendor.name=Google -Didea.paths.selector=%STUDIO_VERSION%.safe "-Djna.boot.library.path=%IDE_HOME%/lib/jna/amd64" "-Dpty4j.preferred.native.folder=%IDE_HOME%/lib/pty4j" -Djna.nosys=true -Djna.noclasspath=true -Didea.platform.prefix=AndroidStudio -Dintellij.custom.startup.error.reporting.url=https://issuetracker.google.com/issues/new?component=192708 -XX:FlightRecorderOptions=stackdepth=256 --add-opens=java.base/sun.net.www.protocol.https=ALL-UNNAMED -Didea.required.plugins.id=org.jetbrains.kotlin -Djava.security.manager=allow -Dsplash=true -Daether.connector.resumeDownloads=false --add-opens=java.base/java.util.concurrent.locks=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED --add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.lang.ref=ALL-UNNAMED --add-opens=java.base/java.lang.reflect=ALL-UNNAMED --add-opens=java.base/java.net=ALL-UNNAMED --add-opens=java.base/java.nio=ALL-UNNAMED --add-opens=java.base/java.nio.charset=ALL-UNNAMED --add-opens=java.base/java.text=ALL-UNNAMED --add-opens=java.base/java.time=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED --add-opens=java.base/java.util.concurrent=ALL-UNNAMED --add-opens=java.base/java.util.concurrent.atomic=ALL-UNNAMED --add-opens=java.base/jdk.internal.vm=ALL-UNNAMED --add-opens=java.base/sun.nio.ch=ALL-UNNAMED --add-opens=java.base/sun.nio.fs=ALL-UNNAMED --add-opens=java.base/sun.security.ssl=ALL-UNNAMED --add-opens=java.base/sun.security.util=ALL-UNNAMED --add-opens=java.base/sun.net.dns=ALL-UNNAMED --add-opens=java.desktop/java.awt=ALL-UNNAMED --add-opens=java.desktop/java.awt.dnd.peer=ALL-UNNAMED --add-opens=java.desktop/java.awt.event=ALL-UNNAMED --add-opens=java.desktop/java.awt.image=ALL-UNNAMED --add-opens=java.desktop/java.awt.peer=ALL-UNNAMED --add-opens=java.desktop/java.awt.font=ALL-UNNAMED --add-opens=java.desktop/javax.swing=ALL-UNNAMED --add-opens=java.desktop/javax.swing.plaf.basic=ALL-UNNAMED --add-opens=java.desktop/javax.swing.text.html=ALL-UNNAMED --add-opens=java.desktop/sun.awt.datatransfer=ALL-UNNAMED --add-opens=java.desktop/sun.awt.image=ALL-UNNAMED --add-opens=java.desktop/sun.awt.windows=ALL-UNNAMED --add-opens=java.desktop/sun.awt=ALL-UNNAMED --add-opens=java.desktop/sun.font=ALL-UNNAMED --add-opens=java.desktop/sun.java2d=ALL-UNNAMED --add-opens=java.desktop/sun.swing=ALL-UNNAMED --add-opens=java.desktop/com.sun.java.swing=ALL-UNNAMED --add-opens=jdk.attach/sun.tools.attach=ALL-UNNAMED --add-opens=jdk.compiler/com.sun.tools.javac.api=ALL-UNNAMED --add-opens=jdk.internal.jvmstat/sun.jvmstat.monitor=ALL-UNNAMED --add-opens=jdk.jdi/com.sun.tools.jdi=ALL-UNNAMED ^
  com.intellij.idea.Main ^
  %* disableNonBundledPlugins dontReopenProjects