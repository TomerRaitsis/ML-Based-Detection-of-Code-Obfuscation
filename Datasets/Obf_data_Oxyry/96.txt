from threading import local #line:1
_OOO0OOO00O0O0O0O0 =local ()#line:3
def get_current_context (silent =False ):#line:6
    ""#line:20
    try :#line:21
        return _OOO0OOO00O0O0O0O0 .stack [-1 ]#line:22
    except (AttributeError ,IndexError ):#line:23
        if not silent :#line:24
            raise RuntimeError ("There is no active click context.")#line:25
def push_context (O0OO0OOOOOO0O0OO0 ):#line:28
    ""#line:29
    _OOO0OOO00O0O0O0O0 .__dict__ .setdefault ("stack",[]).append (O0OO0OOOOOO0O0OO0 )#line:30
def pop_context ():#line:33
    ""#line:34
    _OOO0OOO00O0O0O0O0 .stack .pop ()#line:35
def resolve_color_default (color =None ):#line:38
    ""#line:42
    if color is not None :#line:43
        return color #line:44
    OOOOOOO0OOOO00000 =get_current_context (silent =True )#line:45
    if OOOOOOO0OOOO00000 is not None :#line:46
        return OOOOOOO0OOOO00000 .color #line:47
