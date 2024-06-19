from __future__ import unicode_literals #line:17
from .import Infinite #line:18
from .helpers import WriteMixin #line:19
class Spinner (WriteMixin ,Infinite ):#line:22
    message =''#line:23
    phases =('-','\\','|','/')#line:24
    hide_cursor =True #line:25
    def update (O00O00O000OOOO000 ):#line:27
        O00O0O0OOO0O0OOOO =O00O00O000OOOO000 .index %len (O00O00O000OOOO000 .phases )#line:28
        O00O00O000OOOO000 .write (O00O00O000OOOO000 .phases [O00O0O0OOO0O0OOOO ])#line:29
class PieSpinner (Spinner ):#line:32
    phases =['◷','◶','◵','◴']#line:33
class MoonSpinner (Spinner ):#line:36
    phases =['◑','◒','◐','◓']#line:37
class LineSpinner (Spinner ):#line:40
    phases =['⎺','⎻','⎼','⎽','⎼','⎻']#line:41
class PixelSpinner (Spinner ):#line:43
    phases =['⣾','⣷','⣯','⣟','⡿','⢿','⣻','⣽']#line:44
