from __future__ import absolute_import ,division ,print_function #line:4
class Infinity (object ):#line:7
    def __repr__ (OO000OO0O0O00OOOO ):#line:8
        return "Infinity"#line:9
    def __hash__ (OO0O0000O00O0OO0O ):#line:11
        return hash (repr (OO0O0000O00O0OO0O ))#line:12
    def __lt__ (OO0OOOO0O00O0OOOO ,OO0OOO0000000000O ):#line:14
        return False #line:15
    def __le__ (O0O0O00OO00OOOOO0 ,O00000O0O0OOOOOO0 ):#line:17
        return False #line:18
    def __eq__ (OOO00O0000OO000O0 ,O0O0OOOOO0OO0O0O0 ):#line:20
        return isinstance (O0O0OOOOO0OO0O0O0 ,OOO00O0000OO000O0 .__class__ )#line:21
    def __ne__ (OO00OO0000000O0OO ,O00OOO0O000000000 ):#line:23
        return not isinstance (O00OOO0O000000000 ,OO00OO0000000O0OO .__class__ )#line:24
    def __gt__ (O0OOOOO0OOOO00O0O ,O00OOO00OOOOOO000 ):#line:26
        return True #line:27
    def __ge__ (O00000OO00OO0OO0O ,OO00000OOO0O0O000 ):#line:29
        return True #line:30
    def __neg__ (OO00OOO000000000O ):#line:32
        return NegativeInfinity #line:33
Infinity =Infinity ()#line:36
class NegativeInfinity (object ):#line:39
    def __repr__ (OOO000O00OOO0OOO0 ):#line:40
        return "-Infinity"#line:41
    def __hash__ (O0OOOO00O0O00O00O ):#line:43
        return hash (repr (O0OOOO00O0O00O00O ))#line:44
    def __lt__ (O000O00OO00OOOO0O ,O000OO00O0OO00O00 ):#line:46
        return True #line:47
    def __le__ (OOOO0O0OOO0000OO0 ,O000OO0O00000OOOO ):#line:49
        return True #line:50
    def __eq__ (OO0O0O00000OOOOOO ,OOOO0OO000000O000 ):#line:52
        return isinstance (OOOO0OO000000O000 ,OO0O0O00000OOOOOO .__class__ )#line:53
    def __ne__ (O0O0OOO00O00OO000 ,O0O00O00O0OOOO000 ):#line:55
        return not isinstance (O0O00O00O0OOOO000 ,O0O0OOO00O00OO000 .__class__ )#line:56
    def __gt__ (OOO00O000OO0OOO00 ,OO0O000000OOO0OO0 ):#line:58
        return False #line:59
    def __ge__ (OOO0OO0O00O0OO00O ,O0O0000000O000000 ):#line:61
        return False #line:62
    def __neg__ (O0OO00O000OO000OO ):#line:64
        return Infinity #line:65
NegativeInfinity =NegativeInfinity ()#line:68
