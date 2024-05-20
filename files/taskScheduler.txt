Set MY_LOG=C:\System.sav\Logs\Win10HPAudioSwitch.log
set CurrentPath=%~dp0 
set InstallPath="c:\Program Files (x86)\HP\HPAudioSwitch"
pushd %InstallPath%

schtasks /f /delete /tn HPAudioSwitch
schtasks /f /create /tn HPAudioSwitch /xml HPAudioSwitch.xml

popd
Exit