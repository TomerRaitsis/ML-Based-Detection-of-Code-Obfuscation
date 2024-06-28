# Define the path to your script file
$scriptPath = "/home/yossi/Desktop/ML-Based-Detection-of-Code-Obfuscation/Decoding/file_14.txt"

# Define the output path for the DLL file
$outputPath = "/home/yossi/Desktop/ML-Based-Detection-of-Code-Obfuscation/Decoding/output.dll"

# Read the file content
$BKxlg = Get-Content -Path $scriptPath

foreach($epMme in $BKxlg) {
    if($epMme.StartsWith(':: ')) {
        $sKsAK = $epMme.Substring(3)
        break
    }
}

$dOYIS = [System.Convert]::FromBase64String($sKsAK)
$cMTqL = New-Object System.Security.Cryptography.AesManaged
$cMTqL.Mode = [System.Security.Cryptography.CipherMode]::CBC
$cMTqL.Padding = [System.Security.Cryptography.PaddingMode]::PKCS7
$cMTqL.Key = [System.Convert]::FromBase64String('dqRisfLUGTu+hAOZYYcpDZz736uFo7lesFXsGUcOyzA=')
$cMTqL.IV = [System.Convert]::FromBase64String('l0v4Ir7Yiv3HWsvj0m0O+g==')
$wmEAp = $cMTqL.CreateDecryptor()
$dOYIS = $wmEAp.TransformFinalBlock($dOYIS, 0, $dOYIS.Length)
$wmEAp.Dispose()
$cMTqL.Dispose()

# Decompress the data
$ERfEc = New-Object System.IO.MemoryStream(, $dOYIS)
$PYioo = New-Object System.IO.MemoryStream
$lFCGE = New-Object System.IO.Compression.GZipStream($ERfEc, [IO.Compression.CompressionMode]::Decompress)
$lFCGE.CopyTo($PYioo)
$lFCGE.Dispose()
$ERfEc.Dispose()
$PYioo.Dispose()
$dOYIS = $PYioo.ToArray()

# Save the output to a DLL file
[System.IO.File]::WriteAllBytes($outputPath, $dOYIS)

# Uncomment the following lines if you want to load the assembly and invoke its entry point
# $Nuuhp = [System.Reflection.Assembly]::Load($dOYIS)
# $FJKwX = $Nuuhp.EntryPoint
# $FJKwX.Invoke($null, [string[]]@('%*'))

# Output completion message
Write-Host "DLL saved to $outputPath"

