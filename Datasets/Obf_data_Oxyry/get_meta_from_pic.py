from PIL import Image #line:1
from PIL .ExifTags import TAGS #line:2
from author_utils import get_file_security ,get_author #line:3
from gps_utils import get_location #line:4
import os #line:5
import sys #line:6
from datetime import datetime #line:7
def get_exif (O0OO000O0O0000OO0 ):#line:9
    O0OO000O0O0000OO0 .verify ()#line:10
    return O0OO000O0O0000OO0 ._getexif ()#line:11
def get_labeled_exif (OO0O000OOO0O0OOO0 ):#line:14
    OOO000OOOOO0O0O00 ={}#line:15
    for (O00O000O00O00O0OO ,O00O000O00OOO0OOO )in OO0O000OOO0O0OOO0 .items ():#line:16
        OOO000OOOOO0O0O00 [TAGS .get (O00O000O00O00O0OO )]=O00O000O00OOO0OOO #line:17
    return OOO000OOOOO0O0O00 #line:19
im =Image .open (sys .argv [1 ])#line:21
name =im .filename #line:24
w ,h =im .size #line:27
_ ,file_extension =os .path .splitext (sys .argv [1 ])#line:30
exif =get_exif (im )#line:33
labeled =get_labeled_exif (exif )#line:34
ctime =os .path .getctime (sys .argv [1 ])#line:37
print ("ImageName: %s"%(name ))#line:40
print ("size: %sx%s"%(w ,h ))#line:41
print ("FileExtension: %s"%(file_extension ))#line:42
if ('ExifImageWidth'in labeled .keys ()):#line:43
    print ("ImageWidth: %s"%(labeled ['ExifImageWidth']))#line:44
else :#line:45
    print ("No ImageWidth")#line:46
if ('ExifImageHeight'in labeled .keys ()):#line:48
    print ("ImageHeight: %s"%(labeled ['ExifImageHeight']))#line:49
else :#line:50
    print ("No ImageHeight")#line:51
if ('DateTimeOriginal'in labeled .keys ()):#line:53
    print ("DateTimeOriginal: %s"%(labeled ['DateTimeOriginal']))#line:54
else :#line:55
    print ("No DateTimeOriginal")#line:56
print ("CreateDate: %s"%(datetime .fromtimestamp (ctime ).strftime ('%Y-%m-%d %H:%M:%S')))#line:58
print ("Author: %s"%(get_author (sys .argv [1 ])))#line:59
print ("Location: %s"%(get_location (sys .argv [1 ])))#line:60
