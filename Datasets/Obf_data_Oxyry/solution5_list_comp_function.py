#!/usr/bin/env python3
""#line:2
import argparse #line:4
import os #line:5
import re #line:6
def get_args ():#line:10
    ""#line:11
    O0O00OOO0000O0O00 =argparse .ArgumentParser (description ='Apples and bananas',formatter_class =argparse .ArgumentDefaultsHelpFormatter )#line:15
    O0O00OOO0000O0O00 .add_argument ('text',metavar ='text',help ='Input text or file')#line:17
    O0O00OOO0000O0O00 .add_argument ('-v','--vowel',help ='The vowel to substitute',metavar ='vowel',type =str ,default ='a',choices =list ('aeiou'))#line:25
    OO00OOO00O0O0OO00 =O0O00OOO0000O0O00 .parse_args ()#line:27
    if os .path .isfile (OO00OOO00O0O0OO00 .text ):#line:29
        OO00OOO00O0O0OO00 .text =open (OO00OOO00O0O0OO00 .text ).read ().rstrip ()#line:30
    return OO00OOO00O0O0OO00 #line:32
def main ():#line:36
    ""#line:37
    OO00OOOOO0O0O0OO0 =get_args ()#line:39
    O00OO0O0000O0000O =OO00OOOOO0O0O0OO0 .vowel #line:40
    def O00OOOOO00O0O000O (OO00O0O0O00O0000O ):#line:42
        return O00OO0O0000O0000O if OO00O0O0O00O0000O in 'aeiou'else O00OO0O0000O0000O .upper ()if OO00O0O0O00O0000O in 'AEIOU'else OO00O0O0O00O0000O #line:43
    print (''.join ([O00OOOOO00O0O000O (OOO00O0OO0O0O00OO )for OOO00O0OO0O0O00OO in OO00OOOOO0O0O0OO0 .text ]))#line:45
if __name__ =='__main__':#line:49
    main ()#line:50
