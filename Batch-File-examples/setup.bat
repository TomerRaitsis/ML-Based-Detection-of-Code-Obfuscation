reg import "%~dp0packagever.reg" /reg:64
Pushd "%~dp0"
pnputil -i -a *.inf