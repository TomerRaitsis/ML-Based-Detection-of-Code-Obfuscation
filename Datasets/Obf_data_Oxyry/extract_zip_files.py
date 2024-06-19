import os #line:1
import zipfile #line:2
import sys #line:3
import argparse #line:4
parser =argparse .ArgumentParser ()#line:7
parser .add_argument ("-l","--zippedfile",required =True ,help ="Zipped file")#line:8
args =vars (parser .parse_args ())#line:9
zip_file =args ['zippedfile']#line:12
file_name =zip_file #line:14
if os .path .exists (zip_file )==False :#line:17
    sys .exit ("No such file present in the directory")#line:18
def extract (OOOOO0O0OO00000O0 ):#line:21
    OOO0O0O0O00O0O0O0 =OOOOO0O0OO00000O0 .split (".zip")[0 ]#line:22
    if OOOOO0O0OO00000O0 .endswith (".zip"):#line:23
        OOO00OOOO0OOO00O0 =os .getcwd ()#line:26
        O0000O00OO00O000O =OOO00OOOO0OOO00O0 +"/"+OOO0O0O0O00O0O0O0 #line:27
        with zipfile .ZipFile (OOOOO0O0OO00000O0 ,'r')as OO0O00OO00OOOO0OO :#line:29
            OO0O00OO00OOOO0OO .extractall (O0000O00OO00O000O )#line:30
        print ("Extracted successfully!!!")#line:31
    else :#line:32
        print ("Not a zip file")#line:33
extract (zip_file )#line:35
