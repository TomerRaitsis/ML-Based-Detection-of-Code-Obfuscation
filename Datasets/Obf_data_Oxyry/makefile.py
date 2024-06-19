""#line:8
import io #line:9
from socket import SocketIO #line:11
def backport_makefile (OO0O0O0O0O0000000 ,mode ="r",buffering =None ,encoding =None ,errors =None ,newline =None ):#line:15
    ""#line:18
    if not set (mode )<={"r","w","b"}:#line:19
        raise ValueError ("invalid mode %r (only r, w, b allowed)"%(mode ,))#line:22
    O0OOO0OOOO000O000 ="w"in mode #line:23
    O0OOOOO0000O000O0 ="r"in mode or not O0OOO0OOOO000O000 #line:24
    assert O0OOOOO0000O000O0 or O0OOO0OOOO000O000 #line:25
    OO0O0OOO0OO0OOO00 ="b"in mode #line:26
    OO0OO00O0OOOOOO00 =""#line:27
    if O0OOOOO0000O000O0 :#line:28
        OO0OO00O0OOOOOO00 +="r"#line:29
    if O0OOO0OOOO000O000 :#line:30
        OO0OO00O0OOOOOO00 +="w"#line:31
    O000000O0O000OOOO =SocketIO (OO0O0O0O0O0000000 ,OO0OO00O0OOOOOO00 )#line:32
    OO0O0O0O0O0000000 ._makefile_refs +=1 #line:33
    if buffering is None :#line:34
        buffering =-1 #line:35
    if buffering <0 :#line:36
        buffering =io .DEFAULT_BUFFER_SIZE #line:37
    if buffering ==0 :#line:38
        if not OO0O0OOO0OO0OOO00 :#line:39
            raise ValueError ("unbuffered streams must be binary")#line:40
        return O000000O0O000OOOO #line:41
    if O0OOOOO0000O000O0 and O0OOO0OOOO000O000 :#line:42
        O00OOOOOO00000O0O =io .BufferedRWPair (O000000O0O000OOOO ,O000000O0O000OOOO ,buffering )#line:43
    elif O0OOOOO0000O000O0 :#line:44
        O00OOOOOO00000O0O =io .BufferedReader (O000000O0O000OOOO ,buffering )#line:45
    else :#line:46
        assert O0OOO0OOOO000O000 #line:47
        O00OOOOOO00000O0O =io .BufferedWriter (O000000O0O000OOOO ,buffering )#line:48
    if OO0O0OOO0OO0OOO00 :#line:49
        return O00OOOOOO00000O0O #line:50
    OO0OOOO00O00OO0OO =io .TextIOWrapper (O00OOOOOO00000O0O ,encoding ,errors ,newline )#line:51
    OO0OOOO00O00OO0OO .mode =mode #line:52
    return OO0OOOO00O00OO0OO #line:53
