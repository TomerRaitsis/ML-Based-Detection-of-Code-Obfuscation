@if not defined _echo echo off
setlocal ENABLEEXTENSIONS ENABLEDELAYEDEXPANSION

set OUTPUTDIR=%USERPROFILE%\Desktop
set DODUMP=0
set SENDMAIL=0
set RETURNCODE=0
set DecoderKey=
set ScriptName=%~0

REM Set the CAB file name to include the date and time with
REM underscores substituted for the invalid characters.

set DATETIMESUFFIX=%DATE:/=_%_%TIME::=_%
set CABOUTPUT=OneDriveLogs_%DATETIMESUFFIX: =_%.cab

:ParseCommand
if "%~1"=="" goto :ParseDone

if /i "%~1"=="/OutputDir" (
    for %%i in (%2) do set OUTPUTDIR=%%~i
    shift
) else if /i "%~1"=="/OutputFile" (
    for %%i in (%2) do set CABOUTPUT=%%~i
    shift
) else if /i "%~1"=="/NoDump" (
    set DODUMP=0
) else if /i "%~1"=="/SendMail" (
    set SENDMAIL=1
) else if /i "%~1"=="/IncludeDecoderKey" (
    set DecoderKey=Y
) else if /i "%~1"=="/NoDecoderKey" (
    set DecoderKey=N
) else (
    echo Usage: %ScriptName% [Options]
    echo.
    echo     This script collects all the client logs and CABs them up for simple
    echo     upload.  By default, it will drop the CAB file on your Desktop.
    echo.
    echo Options:
    echo.
    echo     /OutputDir outputdirectory   - Set output directory
    echo     /NoDump                      - Don't collect a process dump of OneDrive.exe
    echo     /OutputFile outputFile       - Filename of output file to use
    echo     /SendMail                    - Triggers an email to the given alias with the full path of the file.
    echo     /IncludeDecoderKey           - Do not prompt and include the decoder key with the logs
    echo     /NoDecoderKey                - Do not prompt and do NOT include the decoder key with the logs
    echo.
    goto :Return
)
shift
goto :ParseCommand

:ParseDone

REM -------------------------
REM * CLIENT PATH DISCOVERY *
REM -------------------------

if "%LOCALAPPDATA%"=="" (
    set LOCALAPPDATA=%USERPROFILE%\Local Settings\Application Data
)

set CLIENTPATH=%LOCALAPPDATA%\Microsoft\OneDrive
set LEGACY_MACHINE_SETUP_LOGS_PATH=%PROGRAMDATA%\Microsoft OneDrive
set MACHINE_I386_SETUP_LOGS_PATH=%PROGRAMFILES(X86)%\Microsoft OneDrive
set MACHINE_AMD64_SETUP_LOGS_PATH=%ProgramW6432%\Microsoft OneDrive
set UPDATER_SERVICE_NAME=OneDrive Updater Service

if exist "%CLIENTPATH%" (
    goto :CopyLogs
)

if exist "%LEGACY_MACHINE_SETUP_LOGS_PATH%" (
    goto :CopyLogs
)

if exist "%MACHINE_I386_SETUP_LOGS_PATH%" (
    goto :CopyLogs
)

if exist "%MACHINE_AMD64_SETUP_LOGS_PATH%" (
    goto :CopyLogs
)

REM None of the data folders exist, exit.
echo Error: No application data exists for OneDrive client.
echo.
goto :Return

REM -------------
REM * COPY LOGS *
REM -------------

:CopyLogs

if exist "%CLIENTPATH%" (
    pushd "%CLIENTPATH%"
    set WORKINGDIR=%CLIENTPATH%\LogCollection
) else (
    set WORKINGDIR=%TMP%\LogCollection
)

if exist "%WORKINGDIR%" (
    rd /s /q "%WORKINGDIR%"
)

mkdir "%WORKINGDIR%"

echo.
echo Microsoft values your privacy.
echo.
echo You have been asked to provide logs from your computer that will help support
echo engineers identify and resolve a problem you have been experiencing.
echo.
echo Text such as web addresses (URLs), email addresses, File and Folder names that
echo are in the logs are scrambled so the original text is not visible to engineers
echo investigating your logs.
echo.

if not defined DecoderKey (
    echo Giving support engineers the ability to unscramble your logs will allow
    echo trouble shooting issues you are having with specific files or folders. Without
    echo this ability, you may need to perform additional manual steps to provide
    echo support with information they need to troubleshoot your issue.
    echo.
    echo May support unscramble your logs?
    set /p DecoderKey=Enter YES or NO: 
    echo.
)

if /I "%DecoderKey:~0,1%" == "Y" (
  set SyncLogsExclude=
  set SyncSettingsExclude=
  echo You have given support the ability to unscramble your logs.
) else (
  set SyncLogsExclude=/XF ObfuscationStringMap.txt *.keystore
  set SyncSettingsExclude=/XF *.dat
  echo Support will not be able to unscramble your logs.
  echo.
  echo Microsoft may need you to perform extra steps to troubleshoot your issue.
)
echo.

REM If the user wants to include their DecoderKey, check if Vault has been setup for their Personal instance
REM If it has, prompt the user to ask if they would like to include their Vault encryption key store
if /I "%DecoderKey:~0,1%" == "Y" (
    set PERSONAL_ACCOUNT_REGISTRY_KEY="HKCU\Software\Microsoft\OneDrive\Accounts\Personal"
    reg.exe QUERY !PERSONAL_ACCOUNT_REGISTRY_KEY! /v VaultIntroShown | find "0x1" 2>&1>NUL
    if !ERRORLEVEL! == 0 (
        set VaultSetupComplete=Y
    )

    if defined VaultSetupComplete (
        echo Would you also like to give support engineers the ability to unscramble
        echo your Personal Vault logs? This is important if you are experiencing issues
        echo while using your Personal Vault. 
        echo If you select "Yes" you will be prompted to unlock your Vault
        echo.
        echo May support unscramble your Personal Vault logs?
        set /p VaultDecoderKey=Enter YES or NO: 
        echo.
    )

    set ONEDRIVE_EXE_PATH=%~dp0..\OneDrive.exe

    if /I "!VaultDecoderKey:~0,1!" == "Y" (
        !ONEDRIVE_EXE_PATH! /outputkeystorevault
        echo After you have unlocked your Personal Vault or you would no longer like to give
        echo support engineers the ability to unscramble your Vault logs, press any key to continue.
        pause
    )
)

echo Working directory is %WORKINGDIR%.
echo OutputDir is %OutputDir%
echo OutputFile is %CabOutput%
echo DoDump is %DoDump%
echo SendMail is %SendMail%
echo.
echo Gathering Logs ...
echo.

set > "%WORKINGDIR%\env.txt"
REM TaskList and SystemInfo are not available on XP Home.
REM /v makes tasklist.exe really slow when not running elevated so don't use it
tasklist.exe > "%WORKINGDIR%\tasklist.txt"
systeminfo.exe > "%WORKINGDIR%\systeminfo.txt"

REM Capture list of running services.
net.exe start > "%WORKINGDIR%\services.txt"

REM Capture fltmc.exe output (will fail if not elevated)
fltmc.exe > "%WORKINGDIR%\fltmc.txt"

REM Capture service information for OneDrive Updater Service
sc.exe query "%UPDATER_SERVICE_NAME%" > "%WORKINGDIR%\updaterservice.txt"
sc.exe qc "%UPDATER_SERVICE_NAME%" >> "%WORKINGDIR%\updaterservice.txt"

REM OneDrive
set /p CRLF=Copying OneDrive logs <NUL

set WORKINGDIRONEDRIVE=%WORKINGDIR%\OneDrive
mkdir "%WORKINGDIRONEDRIVE%"

if exist "%CLIENTPATH%" (
    dir /S "%CLIENTPATH%" > "%WORKINGDIRONEDRIVE%\tree.txt"
    robocopy.exe "%CLIENTPATH%\logs" "%WORKINGDIRONEDRIVE%\logs" /S %SyncLogsExclude%
    robocopy.exe "%CLIENTPATH%\settings" "%WORKINGDIRONEDRIVE%\settings" /S %SyncSettingsExclude%
    robocopy.exe "%CLIENTPATH%\setup\logs" "%WORKINGDIRONEDRIVE%\setup\logs" /S
)

if exist "%LEGACY_MACHINE_SETUP_LOGS_PATH%" (
    robocopy.exe "%LEGACY_MACHINE_SETUP_LOGS_PATH%\setup\logs" "%WORKINGDIRONEDRIVE%\LegacyMachineSetupLogs\setup\logs" /S
    robocopy.exe "%LEGACY_MACHINE_SETUP_LOGS_PATH%\StandaloneUpdater\logs" "%WORKINGDIRONEDRIVE%\LegacyMachineSetupLogs\StandaloneUpdater\logs" /S
    robocopy.exe "%LEGACY_MACHINE_SETUP_LOGS_PATH%\UpdaterService\logs" "%WORKINGDIRONEDRIVE%\LegacyMachineSetupLogs\UpdaterService\logs" /S
    robocopy.exe "%LEGACY_MACHINE_SETUP_LOGS_PATH%\FileSyncHelper\logs" "%WORKINGDIRONEDRIVE%\LegacyMachineSetupLogs\FileSyncHelper\logs" /S
)

if exist "%MACHINE_I386_SETUP_LOGS_PATH%" (
    robocopy.exe "%MACHINE_I386_SETUP_LOGS_PATH%\setup\logs" "%WORKINGDIRONEDRIVE%\MachineSetupLogs\setup\logs" /S
    robocopy.exe "%MACHINE_I386_SETUP_LOGS_PATH%\StandaloneUpdater\logs" "%WORKINGDIRONEDRIVE%\MachineSetupLogs\StandaloneUpdater\logs" /S
    robocopy.exe "%MACHINE_I386_SETUP_LOGS_PATH%\UpdaterService\logs" "%WORKINGDIRONEDRIVE%\MachineSetupLogs\UpdaterService\logs" /S
    robocopy.exe "%MACHINE_I386_SETUP_LOGS_PATH%\FileSyncHelper\logs" "%WORKINGDIRONEDRIVE%\MachineSetupLogs\FileSyncHelper\logs" /S
)

if exist "%MACHINE_AMD64_SETUP_LOGS_PATH%" (
    robocopy.exe "%MACHINE_AMD64_SETUP_LOGS_PATH%\setup\logs" "%WORKINGDIRONEDRIVE%\MachineAmd64SetupLogs\setup\logs" /S
    robocopy.exe "%MACHINE_AMD64_SETUP_LOGS_PATH%\StandaloneUpdater\logs" "%WORKINGDIRONEDRIVE%\MachineAmd64SetupLogs\StandaloneUpdater\logs" /S
    robocopy.exe "%MACHINE_AMD64_SETUP_LOGS_PATH%\UpdaterService\logs" "%WORKINGDIRONEDRIVE%\MachineAmd64SetupLogs\UpdaterService\logs" /S
    robocopy.exe "%MACHINE_AMD64_SETUP_LOGS_PATH%\FileSyncHelper\logs" "%WORKINGDIRONEDRIVE%\MachineAmd64SetupLogs\FileSyncHelper\logs" /S
)

set PERMACHINECLIENTPATH86=%PROGRAMFILES(X86)%\Microsoft OneDrive
if exist "%PERMACHINECLIENTPATH86%" (
    dir /S "%PERMACHINECLIENTPATH86%" > "%WORKINGDIRONEDRIVE%\PerMachine86Tree.txt"
)

set PERMACHINECLIENTPATH64=%ProgramW6432%\Microsoft OneDrive
if exist "%PERMACHINECLIENTPATH64%" (
    dir /S "%PERMACHINECLIENTPATH64%" > "%WORKINGDIRONEDRIVE%\PerMachine64Tree.txt"
)

REM Collect start menu shortcut state
set PERMACHINE_START_MENU_KEY="HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"
for /f "tokens=4*" %%i in (
    'reg.exe QUERY !PERMACHINE_START_MENU_KEY! /v "Common Start Menu"'
) do (
    call set PERMACHINE_START_MENU_PATH=%%~j
)
set PERMACHINE_START_MENU_PATH="%PERMACHINE_START_MENU_PATH%\Programs\OneDrive.lnk"

set PERUSER_START_MENU_KEY="HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
for /f "tokens=3*" %%i in (
    'reg.exe QUERY !PERUSER_START_MENU_KEY! /v "Start Menu"'
) do (
    call set PERUSER_START_MENU_PATH=%%~j
)
set PERUSER_START_MENU_PATH="%PERUSER_START_MENU_PATH%\Programs\OneDrive.lnk"

if exist %PERUSER_START_MENU_PATH% (
    echo PerUser start menu shortcut exists at %PERUSER_START_MENU_PATH% > "%WORKINGDIRONEDRIVE%\StartMenuShortcut.txt"
) else (
    echo PerUser start menu shortcut does not exist at %PERUSER_START_MENU_PATH% > "%WORKINGDIRONEDRIVE%\StartMenuShortcut.txt"
)

if exist %PERMACHINE_START_MENU_PATH% (
    echo PerMachine start menu shortcut exists at %PERMACHINE_START_MENU_PATH% >> "%WORKINGDIRONEDRIVE%\StartMenuShortcut.txt"
) else (
    echo PerMachine start menu shortcut does not exist at %PERMACHINE_START_MENU_PATH% >> "%WORKINGDIRONEDRIVE%\StartMenuShortcut.txt"
)


REM Collect list of overlay handlers
CALL :LogRegkey "\Microsoft\Windows\CurrentVersion\Explorer\ShellIconOverlayIdentifiers", "/s", "%WORKINGDIRONEDRIVE%\reg_OverlayHandlers.txt", HKLM\Software

REM Collect Run key and RunOnce key
CALL :LogRegkey "\Microsoft\Windows\CurrentVersion\Run", "/s", "%WORKINGDIRONEDRIVE%\reg_RunKeys.txt", HKCU\Software
CALL :LogRegkey "\Microsoft\Windows\CurrentVersion\RunOnce", "/s", "%WORKINGDIRONEDRIVE%\reg_RunKeys.txt", HKCU\Software

REM Collect OneDrive reg keys from HKLM and HKCU
CALL :LogRegkey "\Microsoft\OneDrive", "/s", "%WORKINGDIRONEDRIVE%\reg_OneDriveRegKeys.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node

REM Collect SyncEngineProvider keys
CALL :LogRegkey "\SyncEngines\Providers\OneDrive", "/s", "%WORKINGDIRONEDRIVE%\reg_SyncEngineProviders.txt", HKCU\Software

REM Collect odopen keys
CALL :LogRegkey "\Classes\odopen", "/s", "%WORKINGDIRONEDRIVE%\reg_ODOpen.txt", HKCU\Software, HKLM\Software

REM Collect ARP keys
CALL :LogRegkey "\Microsoft\Windows\CurrentVersion\Uninstall\OneDriveSetup.exe", "/s", "%WORKINGDIRONEDRIVE%\reg_ARP.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node

REM Collect Autoplay handler keys
CALL :LogRegkey "\Microsoft\Windows\CurrentVersion\Explorer\AutoplayHandlers", "/s", "%WORKINGDIRONEDRIVE%\reg_AutoplayHandlers.txt", HKCU\Software

REM Collect policies
CALL :LogRegkey "\Policies\Microsoft\OneDrive", "/s", "%WORKINGDIRONEDRIVE%\reg_OneDrivePolicies.txt", HKLM\Software, HKCU\Software
CALL :LogRegkey "\Policies\Microsoft\Windows\OneDrive", "/s", "%WORKINGDIRONEDRIVE%\reg_OneDrivePolicies.txt", HKLM\Software, HKLM\Software\WOW6432Node

REM Collect Groove keys
CALL :LogRegkey "\Microsoft\Common\Groove", "", "%WORKINGDIRONEDRIVE%\reg_GrooveKeys.txt", HKCU\Software

REM Collect Winlogon keys
CALL :LogRegkey "\Microsoft\Windows NT\CurrentVersion\Winlogon", "", "%WORKINGDIRONEDRIVE%\reg_Winlogon.txt", HKCU\Software, HKLM\Software

REM Collect SyncRootManager keys
CALL :LogRegkey "\Microsoft\Windows\CurrentVersion\Explorer\SyncRootManager", "/s", "%WORKINGDIRONEDRIVE%\reg_SyncRootManagerRegKeys.txt", HKLM\Software

REM Collect COM keys for Current User
CALL :LogRegkey "\Classes\AppID\{EEABD3A3-784D-4334-AAFC-BB13234F17CF}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\AppID\OneDrive.EXE", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\CLSID\{6bb93b4e-44d8-40e2-bd97-42dbcf18a40f}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\SyncEngineCOMServer.SyncEngineCOMServer.1", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\SyncEngineCOMServer.SyncEngineCOMServer", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\CLSID\{AB807329-7324-431B-8B36-DBD581F56E0B}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\SyncEngineStorageProviderHandlerProxy.SyncEngineStorageProviderHandlerProxy.1", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\SyncEngineStorageProviderHandlerProxy.SyncEngineStorageProviderHandlerProxy", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\CLSID\{A3CA1CF4-5F3E-4AC0-91B9-0D3716E1EAC3}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\TypeLib\{638805C3-4BA3-4AC8-8AAC-71A0BA2BC284}\1.0", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\TypeLib\{082D3FEC-D0D0-4DF6-A988-053FECE7B884}\1.0", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\FileSyncClient.FileSyncClient.1", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\FileSyncClient.FileSyncClient", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\CLSID\{7B37E4E2-C62F-4914-9620-8FB5062718CC}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\FileSyncClient.AutoPlayHandler.1", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\FileSyncClient.AutoPlayHandler", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\CLSID\{5999E1EE-711E-48D2-9884-851A709F543D}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\BannerNotificationHandler.BannerNotificationHandler.1", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\BannerNotificationHandler.BannerNotificationHandler", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\CLSID\{2e7c0a19-0438-41e9-81e3-3ad3d64f55ba}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{F0AF7C30-EAE4-4644-961D-54E6E28708D6}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{9D613F8A-B30E-4938-8490-CB5677701EBF}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{79A2A54C-3916-41FD-9FAB-F26ED0BBA755}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{0299ECA9-80B6-43C8-A79A-FB1C5F19E7D8}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{0f872661-c863-47a4-863f-c065c182858a}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{da82e55e-fa2f-45b3-aec3-e7294106ef52}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{e9de26a1-51b2-47b4-b1bf-c87059cc02a7}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{2692D1F2-2C7C-4AE0-8E73-8F37736C912D}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{5D5DD08F-A10E-4FEF-BCA7-E73E666FC66C}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{EE15BBBB-9E60-4C52-ABCB-7540FF3DF6B3}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{8D3F8F15-1DE1-4662-BF93-762EABE988B2}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{2B865677-AC3A-43BD-B9E7-BF6FCD3F0596}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{ACDB5DB0-C9D5-461C-BAAA-5DCE0B980E40}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{909A6CCD-6810-46C4-89DF-05BE7EB61E6C}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{10C9242E-D604-49B5-99E4-BF87945EF86C}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{F062BA81-ADFE-4A92-886A-23FD851D6406}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{3A4E62AE-45D9-41D5-85F5-A45B77AB44E5}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{390AF5A7-1390-4255-9BC9-935BFCFA5D57}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{1196AE48-D92B-4BC7-85DE-664EC3F761F1}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{D0ED5C72-6197-4AAD-9B16-53FE461DD85C}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{AF60000F-661D-472A-9588-F062F6DB7A0E}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{b5c25645-7426-433f-8a5f-42b7ff27a7b2}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{1b7aed4f-fcaf-4da4-8795-c03e635d8edc}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{0d4e4444-cb20-4c2b-b8b2-94e5656ecae8}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{d8c80ebb-099c-4208-afa3-fbc4d11f8a3c}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{C2FE84F5-E036-4A07-950C-9BFD3EAB983A}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{a7126d4c-f492-4eb9-8a2a-f673dbdd3334}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{c1439245-96b4-47fc-b391-679386c5d40f}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{02C98E2C-6C9F-49F8-9B57-3A6E1AA09A67}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{385ED83D-B50C-4580-B2C3-9E64DBE7F511}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{8B9F14F4-9559-4A3F-B7D0-312E992B6D98}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{22A68885-0FD9-42F6-9DED-4FB174DC7344}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{9E1CD0DF-72E7-4284-9598-342C0A46F96B}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{944903E8-B03F-43A0-8341-872200D2DA9C}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{B54E7079-90C9-4C62-A6B8-B2834C33A04A}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{1B71F23B-E61F-45C9-83BA-235D55F50CF9}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{EA23A664-A558-4548-A8FE-A6B94D37C3CF}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{2F12C599-7AA5-407A-B898-09E6E4ED2D1E}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{2EB31403-EBE0-41EA-AE91-A1953104EA55}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{AEEBAD4E-3E0A-415B-9B94-19C499CD7B6A}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{fac14b75-7862-4ceb-be41-f53945a61c17}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\TypeLib\{BAE13F6C-0E2A-4DEB-AA46-B8F55319347C}\1.0", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\CLSID\{BBACC218-34EA-4666-9D7A-C78F2274A524}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\CLSID\{5AB7172C-9C11-405C-8DD5-AF20F3606282}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\CLSID\{A78ED123-AB77-406B-9962-2A5D9D2F7F30}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\CLSID\{A0396A93-DC06-4AEF-BEE9-95FFCCAEF20E}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\CLSID\{F241C880-6982-4CE5-8CF7-7085BA96DA5A}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\CLSID\{9AA2F32D-362A-42D9-9328-24A483E2CCC3}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\CLSID\{C5FF006E-2AE9-408C-B85B-2DFDD5449D9C}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\CLSID\{7AFDFDDB-F914-11E4-8377-6C3BE50D980C}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\CLSID\{82CA8DE3-01AD-4CEA-9D75-BE4C51810A9E}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\CLSID\{1BF42E4C-4AF4-4CFD-A1A0-CF2960B8F63E}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\CLSID\{CB3D0F55-BC2C-4C1A-85ED-23ED75B5106B}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\*\shellex\ContextMenuHandlers\ FileSyncEx", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Directory\Background\shellex\ContextMenuHandlers\ FileSyncEx", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Directory\shellex\ContextMenuHandlers\ FileSyncEx", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\IE.AssocFile.URL\shellex\ContextMenuHandlers\ FileSyncEx", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\lnkfile\shellex\ContextMenuHandlers\ FileSyncEx", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\CLSID\{CB3D0F55-BC2C-4C1A-85ED-23ED75B5106B}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\CLSID\{021E4F06-9DCC-49AD-88CF-ECC2DA314C8A}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{31508CC7-9BC7-494B-9D0F-7B1C7F144182}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\TypeLib\{C9F3F6BB-3172-4CD8-9EB7-37C9BE601C87}\1.0", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\OOBERequestHandler.OOBERequestHandler.1", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\OOBERequestHandler.OOBERequestHandler", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\CLSID\{94269C4E-071A-4116-90E6-52E557067E4E}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\SyncEngineFileInfoProvider.SyncEngineFileInfoProvider.1", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\SyncEngineFileInfoProvider.SyncEngineFileInfoProvider", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\CLSID\{71DCE5D6-4B57-496B-AC21-CD5B54EB93FD}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{466F31F7-9892-477E-B189-FA5C59DE3603}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{869BDA08-7ACF-42B8-91AE-4D8D597C0B33}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{679EC955-75AA-4FB2-A7ED-8C0152ECF409}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\CLSID\{389510b7-9e58-40d7-98bf-60b911cb0ea9}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\CLSID\{9489FEB2-1925-4D01-B788-6D912C70F7F2}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\CLSID\{4410DC33-BC7C-496B-AA84-4AEA3EEE75F7}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{B05D37A9-03A2-45CF-8850-F660DF0CBF07}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{6A821279-AB49-48F8-9A27-F6C59B4FF024}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{4410DC33-BC7C-496B-AA84-4AEA3EEE75F7}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\CLSID\{A926714B-7BFC-4D08-A035-80021395FFA8}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{162C6FB5-44D3-435B-903D-E613FA093FB5}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node
CALL :LogRegkey "\Classes\Interface\{301DFBE5-524C-4B0F-8B2D-21C40B3A2988}", "/s", "%WORKINGDIRONEDRIVE%\reg_COM.txt", HKCU\Software, HKLM\Software, HKLM\Software\WOW6432Node

REM Check if OneDrive is elevated
powershell -Command "& {get-process onedrive | add-member -Name Elevated -MemberType ScriptProperty -Value {if ($this.Name -in @('Idle','System')) {$null} else {-not $this.Path -and -not $this.Handle} } -PassThru | Format-Table Name,Elevated}" > "%WORKINGDIRONEDRIVE%\OneDriveElevated.txt" 2>&1

REM Check if Sparse Package exists for Win 11 OS only.
REM 'ver' will output "Microsoft Windows [Version 10.0.19043.1110]"
REM Split output by spaces or periods. Take the 6th spot which is the build version (19043) and check if it's greater than the min build for Win 11
REM If so, print the package output into OneDriveSparsePackage.txt
for /f "tokens=6 delims=. " %%i in ('ver') do set OSVERSION=%%i
if "%OSVERSION%" gtr "21600" (
    echo Checking Sparse Package information
    powershell -Command "Get-AppxPackage -Name "Microsoft.OneDriveSync" > "%WORKINGDIRONEDRIVE%\OneDriveSparsePackage.txt" 2>&1
)

REM -------------
REM * Export Event logs *
REM -------------
echo.
echo Exporting event logs...
wevtutil.exe export-log Application "%WORKINGDIR%\Application.evtx"
wevtutil.exe export-log System "%WORKINGDIR%\System.evtx"
wevtutil.exe export-log Setup "%WORKINGDIR%\Setup.evtx"
wevtutil.exe export-log Microsoft-Windows-Bits-Client/Operational "%WORKINGDIR%\Bits.evtx"
wevtutil.exe export-log Microsoft-Windows-TaskScheduler/Operational "%WORKINGDIR%\TaskScheduler.evtx"

REM -------------
REM * Export OneDrive Standalone Update Task information *
REM -------------
echo.
echo Exporting OneDrive Standalone Update Task information...
schtasks.exe /query /TN "OneDrive Standalone Update Task" /XML > %WORKINGDIR%\OneDriveStandaloneUpdateTask.xml 2>&1
schtasks.exe /query /TN "OneDrive Standalone Update Task v2" /XML > %WORKINGDIR%\OneDriveStandaloneUpdateTaskV2.xml 2>&1
schtasks.exe /query /TN "OneDrive Per-Machine Standalone Update Task" /XML > %WORKINGDIR%\OneDrivePerMachineStandaloneUpdateTask.xml 2>&1

for /f "skip=6 tokens=2" %%i IN ('whoami /user') do set SID=%%i
schtasks.exe /query /TN "OneDrive Standalone Update Task-%SID%" /XML > %WORKINGDIR%\OneDriveStandaloneUpdateTaskSID.xml 2>&1

echo.
echo.


REM Copy complete.  CAB up files.

echo Writing CAB file to %CABOUTPUT%...

call :CABIT "%WORKINGDIR%"

if "%OUTPUTDIR%"=="%USERPROFILE%\Desktop" (
    set SHFOLDER_REGISTRY_KEY="HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
    for /f "tokens=2*" %%i in (
        'reg.exe QUERY !SHFOLDER_REGISTRY_KEY! /v Desktop'
    ) do (
        call set OUTPUTDIR=%%~j
    )
)

if not exist "%OUTPUTDIR%\" (
    echo Error! %OUTPUTDIR% does not exist.
    move /y "%WORKINGDIR%\%CABOUTPUT%" %USERPROFILE%\Desktop\. 2>&1>NUL
    set RETURNCODE=1
    goto :Return    
)

move /y "%WORKINGDIR%\%CABOUTPUT%" "%OUTPUTDIR%\." 2>&1>NUL

if ERRORLEVEL 1 (
    echo error level 1
    move /y "%WORKINGDIR%\%CABOUTPUT%" %USERPROFILE%\Desktop\. 2>&1>NUL
    set RETURNCODE=1
)


rd /s /q "%WORKINGDIR%"

echo.
echo Log collection complete.  Please upload the following file:
echo.
echo     %OUTPUTDIR%\%CABOUTPUT%
echo.

if "%SENDMAIL%"=="1" (
    echo Sending mail...
    call :SendMail
)
goto :Return

REM ---- END OF MAIN SCRIPT ---- Sub-Routines follow ----

REM -----------
REM * CAB IT! *
REM -----------
:CABIT
set DIRECTIVEFILE=%TEMP%\Schema.ddf
set TARGET=%1
set TEMPFILE=%TEMP%\TEMP-%RANDOM%.tmp

if not exist %TARGET% (
    echo %TARGET% does not exist.
    goto :Return
)

pushd %TARGET%

echo. > %DIRECTIVEFILE%
echo .set CabinetNameTemplate=%CABOUTPUT% >> %DIRECTIVEFILE%
echo .set DiskDirectoryTemplate= >> %DIRECTIVEFILE%
echo .set InfFileName=%TEMPFILE% >> %DIRECTIVEFILE%
echo .set RptFileName=%TEMPFILE% >> %DIRECTIVEFILE%
echo .set MaxDiskSize=0 >> %DIRECTIVEFILE%
echo .set CompressionType=LZX >> %DIRECTIVEFILE%

del /f %TEMPFILE% 2>NUL

call :CAB_DIR .

makecab.exe /f %DIRECTIVEFILE%

del /f %DIRECTIVEFILE% 2>NUL
del /f %TEMPFILE% 2>NUL

popd
goto :Return

REM CAB Helper
:CAB_DIR
echo .set DestinationDir=%1 >> %DIRECTIVEFILE%
for /f "tokens=*" %%i in ('dir /b /a:-d %1') do (
    echo "%~1\%%i" >> %DIRECTIVEFILE%
)
for /f "tokens=*" %%i in ('dir /b /a:d %1') do (
    call :CAB_DIR "%~1\%%i"
)
goto :Return

REM Calls reg.exe query on the given regkey and appends output to the given file.
REM If regkey didn't exist, logs that it was not found.
REM Parameter 1: regkey subpath (anything after HKLM\Software, HKCU\Software, or HKLM\Software\WOW6432Node etc.)
REM Parameter 2: params for reg query (e.g. /s)
REM Parameter 3: output file to append to
REM Paramter 4 - n: regkey prefixes to query. E.g. HKLM\Software, HKCU\Software, HKLM\Software\WOW6432Node etc.
:LogRegkey
set argCount=0
for %%x in (%*) do (
    set /a argCount+=1
    if !argCount! GTR 3 (
        reg.exe query "%%x%~1" > nul 2>&1
        if !ERRORLEVEL! EQU 0 (
            reg.exe query "%%x%~1" %~2 >> "%~3" 2>&1
        ) ELSE (
            echo "%%x%~1" NOT FOUND >> "%~3"
        )
    )
)
goto :Return

:SendMail
start mailto:wldrxireport@microsoft.com?subject=[Issue%%20Reporter%%20Logs]%%20New%%20logs%%20from%%20%computername%^&body=A%%20new%%20set%%20of%%20logs%%20have%%20been%%20submitted%%20from%%20device%%20%computername%.%%20The%%20logs%%20can%%20be%%20found%%20here:%%0D%%0A%%20%OUTPUTDIR%\%CabOutput%%%0D%%0A%%0D%%0AYou%%20can%%20reference%%20this%%20report%%20at%%20any%%20time%%20by%%20mailing%%20the%%20wldrxireport%%20alias%%20and%%20including%%20the%%20following%%20report%%20identifier:%%0D%%0A%CabOutput%%%0D%%0A%%0D%%0A(Optional)%%20additional%%20comments/repro%%20steps:"
goto :Return

:Return
exit /b %RETURNCODE%