@echo off
"C:\\Program Files\\Java\\jdk-17\\bin\\java" ^
  --class-path ^
  "C:\\Users\\efrat\\.gradle\\caches\\modules-2\\files-2.1\\com.google.prefab\\cli\\2.0.0\\f2702b5ca13df54e3ca92f29d6b403fb6285d8df\\cli-2.0.0-all.jar" ^
  com.google.prefab.cli.AppKt ^
  --build-system ^
  cmake ^
  --platform ^
  android ^
  --abi ^
  x86_64 ^
  --os-version ^
  23 ^
  --stl ^
  c++_shared ^
  --ndk-version ^
  25 ^
  --output ^
  "C:\\Users\\efrat\\AppData\\Local\\Temp\\agp-prefab-staging15855441711182039940\\staged-cli-output" ^
  "C:\\Users\\efrat\\.gradle\\caches\\transforms-3\\043814979a7351adeafae334529a11be\\transformed\\jetified-react-android-0.73.6-debug\\prefab" ^
  "C:\\Users\\efrat\\.gradle\\caches\\transforms-3\\20e14a3a1faed9ce3da9af0343545221\\transformed\\jetified-fbjni-0.5.1\\prefab"
