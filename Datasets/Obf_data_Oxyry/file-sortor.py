import os #line:1
import shutil #line:2
os .chdir ("E:\downloads")#line:3
files =os .listdir ()#line:4
extentions ={"images":[".jpg",".png",".jpeg",".gif"],"videos":[".mp4",".mkv"],"musics":[".mp3",".wav"],"zip":[".zip",".tgz",".rar",".tar"],"documents":[".pdf",".docx",".csv",".xlsx",".pptx",".doc",".ppt",".xls"],"setup":[".msi",".exe"],"programs":[".py",".c",".cpp",".php",".C",".CPP"],"design":[".xd",".psd"]}#line:5
def sorting (OOOO0O00000OO0OO0 ):#line:6
    OO0000O00OO00OOOO =list (extentions .keys ())#line:7
    for OOO0O0O0O000OOOOO in OO0000O00OO00OOOO :#line:8
        for OO0O00OO0OOOO0OO0 in extentions [OOO0O0O0O000OOOOO ]:#line:9
            if OOOO0O00000OO0OO0 .endswith (OO0O00OO0OOOO0OO0 ):#line:10
                return OOO0O0O0O000OOOOO #line:11
for file in files :#line:12
    dist =sorting (file )#line:13
    if dist :#line:14
        try :#line:15
            shutil .move (file ,"../download-sorting/"+dist )#line:16
        except :#line:17
            print (file +" is already exist")#line:18
    else :#line:19
        try :#line:20
            shutil .move (file ,"../download-sorting/others")#line:21
        except :#line:22
            print (file +" is already exist")#line:23
