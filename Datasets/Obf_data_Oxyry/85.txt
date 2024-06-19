import codecs #line:1
import locale #line:2
import re #line:3
import sys #line:4
from pip ._internal .utils .typing import MYPY_CHECK_RUNNING #line:6
if MYPY_CHECK_RUNNING :#line:8
    from typing import List ,Tuple ,Text #line:9
BOMS =[(codecs .BOM_UTF8 ,'utf8'),(codecs .BOM_UTF16 ,'utf16'),(codecs .BOM_UTF16_BE ,'utf16-be'),(codecs .BOM_UTF16_LE ,'utf16-le'),(codecs .BOM_UTF32 ,'utf32'),(codecs .BOM_UTF32_BE ,'utf32-be'),(codecs .BOM_UTF32_LE ,'utf32-le'),]#line:19
ENCODING_RE =re .compile (br'coding[:=]\s*([-\w.]+)')#line:21
def auto_decode (OOOO000OO0O000O0O ):#line:24
    ""#line:28
    for O00O00OO00O00O000 ,OOOO0OO0OO0O0OOOO in BOMS :#line:29
        if OOOO000OO0O000O0O .startswith (O00O00OO00O00O000 ):#line:30
            return OOOO000OO0O000O0O [len (O00O00OO00O00O000 ):].decode (OOOO0OO0OO0O0OOOO )#line:31
    for O0O0O00OO0O000O00 in OOOO000OO0O000O0O .split (b'\n')[:2 ]:#line:33
        if O0O0O00OO0O000O00 [0 :1 ]==b'#'and ENCODING_RE .search (O0O0O00OO0O000O00 ):#line:34
            OOOO0OO0OO0O0OOOO =ENCODING_RE .search (O0O0O00OO0O000O00 ).groups ()[0 ].decode ('ascii')#line:35
            return OOOO000OO0O000O0O .decode (OOOO0OO0OO0O0OOOO )#line:36
    return OOOO000OO0O000O0O .decode (locale .getpreferredencoding (False )or sys .getdefaultencoding (),)#line:39
