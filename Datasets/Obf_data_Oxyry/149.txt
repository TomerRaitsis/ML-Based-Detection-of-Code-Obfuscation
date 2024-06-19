import os #line:1
from PIL import Image #line:2
def watermark_photo (OO00OO0OO0OOO0OOO ,O0O0000OO0OO0OO00 ,O0OOO0OO00O000OO0 ):#line:4
    OOO0OOO00000O00OO =Image .open (OO00OO0OO0OOO0OOO )#line:5
    OO0O00O0O000O0000 =Image .open (O0O0000OO0OO0OO00 ).convert ("RGBA")#line:6
    OOOO0O000OOOO00OO =OOO0OOO00000O00OO .size #line:8
    O0000OOOO0O00O0OO =(int (OOOO0O000OOOO00OO [0 ]*8 /100 ),int (OOOO0O000OOOO00OO [0 ]*8 /100 ))#line:9
    OO0O00O0O000O0000 =OO0O00O0O000O0000 .resize (O0000OOOO0O00O0OO )#line:11
    O0O0OO0OOO0O0O00O =OOOO0O000OOOO00OO [0 ]-O0000OOOO0O00O0OO [0 ]-20 ,OOOO0O000OOOO00OO [1 ]-O0000OOOO0O00O0OO [1 ]-20 #line:15
    OO00O0O0O0O00OO00 =Image .new (mode ='RGBA',size =OOOO0O000OOOO00OO ,color =(0 ,0 ,0 ,0 ))#line:17
    OO00O0O0O0O00OO00 .paste (OOO0OOO00000O00OO ,(0 ,0 ))#line:19
    OO00O0O0O0O00OO00 .paste (OO0O00O0O000O0000 ,O0O0OO0OOO0O0O00O ,OO0O00O0O000O0000 )#line:21
    O0OO0OOO0O0000OOO =OOO0OOO00000O00OO .mode #line:22
    print (O0OO0OOO0O0000OOO )#line:23
    if O0OO0OOO0O0000OOO =='RGB':#line:24
        OO00O0O0O0O00OO00 =OO00O0O0O0O00OO00 .convert (O0OO0OOO0O0000OOO )#line:25
    else :#line:26
        OO00O0O0O0O00OO00 =OO00O0O0O0O00OO00 .convert ('P')#line:27
    OO00O0O0O0O00OO00 .save (O0OOO0OO00O000OO0 ,optimize =True ,quality =100 )#line:28
    print ("Saving"+O0OOO0OO00O000OO0 +"...")#line:29
folder =input ("Enter Folder Path:")#line:31
watermark =input ("Enter Watermark Path:")#line:32
os .chdir (folder )#line:33
files =os .listdir (os .getcwd ())#line:34
print (files )#line:35
if not os .path .isdir ("output"):#line:37
    os .mkdir ("output")#line:38
c =1 #line:40
for f in files :#line:41
    if os .path .isfile (os .path .abspath (f )):#line:42
        if f .endswith (".png")or f .endswith (".jpg"):#line:43
            watermark_photo (f ,watermark ,"output/"+f )#line:44
