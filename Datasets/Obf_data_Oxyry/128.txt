#!/usr/bin/env python3
""#line:2
import argparse #line:4
import os #line:5
import re #line:6
def get_args ():#line:10
    ""#line:11
    OOO0OOO0OOOO000OO =argparse .ArgumentParser (description ='Apples and bananas',formatter_class =argparse .ArgumentDefaultsHelpFormatter )#line:15
    OOO0OOO0OOOO000OO .add_argument ('text',metavar ='text',help ='Input text or file')#line:17
    OOO0OOO0OOOO000OO .add_argument ('-v','--vowel',help ='The vowel to substitute',metavar ='vowel',type =str ,default ='a',choices =list ('aeiou'))#line:25
    O00OOO00000O00000 =OOO0OOO0OOOO000OO .parse_args ()#line:27
    if os .path .isfile (O00OOO00000O00000 .text ):#line:29
        O00OOO00000O00000 .text =open (O00OOO00000O00000 .text ).read ().rstrip ()#line:30
    return O00OOO00000O00000 #line:32
def main ():#line:36
    ""#line:37
    O0O0O000O0000O0O0 =get_args ()#line:39
    print (''.join ([new_char (OO000OO000OOO00O0 ,O0O0O000O0000O0O0 .vowel )for OO000OO000OOO00O0 in O0O0O000O0000O0O0 .text ]))#line:40
def new_char (O0OO00O000OO000O0 ,OOOO00000O0OOO00O ):#line:44
    ""#line:45
    return OOOO00000O0OOO00O if O0OO00O000OO000O0 in 'aeiou'else OOOO00000O0OOO00O .upper ()if O0OO00O000OO000O0 in 'AEIOU'else O0OO00O000OO000O0 #line:48
if __name__ =='__main__':#line:52
    main ()#line:53
