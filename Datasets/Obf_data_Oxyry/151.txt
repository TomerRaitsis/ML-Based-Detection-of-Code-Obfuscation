from __future__ import absolute_import ,division ,unicode_literals #line:1
import re #line:3
from .import base #line:5
from ..constants import rcdataElements ,spaceCharacters #line:6
spaceCharacters ="".join (spaceCharacters )#line:7
SPACES_REGEX =re .compile ("[%s]+"%spaceCharacters )#line:9
class Filter (base .Filter ):#line:12
    ""#line:13
    spacePreserveElements =frozenset (["pre","textarea"]+list (rcdataElements ))#line:14
    def __iter__ (OO0OO00000000OOO0 ):#line:16
        O0O0OO0O0OOOO0O0O =0 #line:17
        for OO0000O0OO0O0OOOO in base .Filter .__iter__ (OO0OO00000000OOO0 ):#line:18
            OOOOOOO00O0O00OO0 =OO0000O0OO0O0OOOO ["type"]#line:19
            if OOOOOOO00O0O00OO0 =="StartTag"and (O0O0OO0O0OOOO0O0O or OO0000O0OO0O0OOOO ["name"]in OO0OO00000000OOO0 .spacePreserveElements ):#line:21
                O0O0OO0O0OOOO0O0O +=1 #line:22
            elif OOOOOOO00O0O00OO0 =="EndTag"and O0O0OO0O0OOOO0O0O :#line:24
                O0O0OO0O0OOOO0O0O -=1 #line:25
            elif not O0O0OO0O0OOOO0O0O and OOOOOOO00O0O00OO0 =="SpaceCharacters"and OO0000O0OO0O0OOOO ["data"]:#line:27
                OO0000O0OO0O0OOOO ["data"]=" "#line:29
            elif not O0O0OO0O0OOOO0O0O and OOOOOOO00O0O00OO0 =="Characters":#line:31
                OO0000O0OO0O0OOOO ["data"]=collapse_spaces (OO0000O0OO0O0OOOO ["data"])#line:32
            yield OO0000O0OO0O0OOOO #line:34
def collapse_spaces (OOO0O0OO00OOO0OOO ):#line:37
    return SPACES_REGEX .sub (' ',OOO0O0OO00OOO0OOO )#line:38
