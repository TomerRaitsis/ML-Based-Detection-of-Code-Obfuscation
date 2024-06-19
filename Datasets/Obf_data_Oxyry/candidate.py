from pip ._vendor .packaging .version import parse as parse_version #line:1
from pip ._internal .utils .models import KeyBasedCompareMixin #line:3
from pip ._internal .utils .typing import MYPY_CHECK_RUNNING #line:4
if MYPY_CHECK_RUNNING :#line:6
    from pip ._vendor .packaging .version import _BaseVersion #line:7
    from pip ._internal .models .link import Link #line:8
    from typing import Any ,Union #line:9
class InstallationCandidate (KeyBasedCompareMixin ):#line:12
    ""#line:14
    def __init__ (OO0OO0OO0OOOO0O0O ,O0OO00000O0O00OO0 ,OOOOOOO0000OO0O00 ,O000O000OOOOOO00O ):#line:16
        OO0OO0OO0OOOO0O0O .project =O0OO00000O0O00OO0 #line:18
        OO0OO0OO0OOOO0O0O .version =parse_version (OOOOOOO0000OO0O00 )#line:19
        OO0OO0OO0OOOO0O0O .location =O000O000OOOOOO00O #line:20
        super (InstallationCandidate ,OO0OO0OO0OOOO0O0O ).__init__ (key =(OO0OO0OO0OOOO0O0O .project ,OO0OO0OO0OOOO0O0O .version ,OO0OO0OO0OOOO0O0O .location ),defining_class =InstallationCandidate )#line:25
    def __repr__ (O0OOOO000O0O00OO0 ):#line:27
        return "<InstallationCandidate({!r}, {!r}, {!r})>".format (O0OOOO000O0O00OO0 .project ,O0OOOO000O0O00OO0 .version ,O0OOOO000O0O00OO0 .location ,)#line:31
