from configparser import ParsingError #line:1
from typing import Optional ,Union #line:2
import pyshorteners #line:4
from pydantic import BaseModel ,PrivateAttr ,ValidationError #line:5
class URLShortener (BaseModel ):#line:8
    url :str #line:9
    _shortener :Optional [pyshorteners .Shortener ]=PrivateAttr ()#line:10
    class Config :#line:12
        arbitrary_types_allowed =True #line:13
    def __init__ (O0000O0OOO000O00O ,**O0OO0O00O00OOO00O ):#line:15
        ""#line:19
        OOO0O00O0000000OO =O0OO0O00O00OOO00O .pop ("shortener",None )or pyshorteners .Shortener ()#line:20
        super ().__init__ (**O0OO0O00O00OOO00O )#line:21
        O0000O0OOO000O00O ._shortener =OOO0O00O0000000OO #line:22
    def shorten_url (O00OOO0O0OOO0O0O0 )->Union [str ,Exception ]:#line:24
        if O00OOO0O0OOO0O0O0 ._shortener is None :#line:25
            raise ValueError ("Shortener is not initialized.")#line:26
        try :#line:28
            return str (O00OOO0O0OOO0O0O0 ._shortener .tinyurl .short (O00OOO0O0OOO0O0O0 .url ))#line:29
        except (ParsingError ,ValidationError )as O000O0O0O00000O00 :#line:30
            return O000O0O0O00000O00 #line:31
        except Exception as OOO00O00O00OOO0OO :#line:32
            return OOO00O00O00OOO0OO #line:33
