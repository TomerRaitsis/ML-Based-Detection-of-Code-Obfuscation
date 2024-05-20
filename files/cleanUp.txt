Set MY_LOG=C:\System.sav\Logs\Win10HPAudioSwitch.log
set CurrentPath=%~dp0 
set InstallPath="c:\Program Files (x86)\HP\HPAudioSwitch"
set UsersPath=c:\Users
pushd %InstallPath%

schtasks /f /delete /tn HPAudioSwitch

popd

rd "C:\ProgramData\HP\HP Audio Switch" /s /q

pushd %UsersPath%
for /d %%u in (*) do rd /s /q "c:\users\%%u\AppData\Roaming\HP\HP Audio Switch"
popd

Exit