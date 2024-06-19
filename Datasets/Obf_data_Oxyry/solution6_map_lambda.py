#!/usr/bin/env python3
""#line:2
import argparse #line:4
import os #line:5
def get_args ():#line:9
    ""#line:10
    O00OO000000O000O0 =argparse .ArgumentParser (description ='Apples and bananas',formatter_class =argparse .ArgumentDefaultsHelpFormatter )#line:14
    O00OO000000O000O0 .add_argument ('text',metavar ='text',help ='Input text or file')#line:16
    O00OO000000O000O0 .add_argument ('-v','--vowel',help ='The vowel to substitute',metavar ='vowel',type =str ,default ='a',choices =list ('aeiou'))#line:24
    OO0O000O0OO0OOO0O =O00OO000000O000O0 .parse_args ()#line:26
    if os .path .isfile (OO0O000O0OO0OOO0O .text ):#line:28
        OO0O000O0OO0OOO0O .text =open (OO0O000O0OO0OOO0O .text ).read ().rstrip ()#line:29
    return OO0O000O0OO0OOO0O #line:31
def main ():#line:35
    ""#line:36
    OOO00OO0O0O0OO000 =get_args ()#line:38
    O0000OO0OO0OOOO00 =OOO00OO0O0O0OO000 .vowel #line:39
    O0O00OOO00OOO00OO =map (lambda O0O00O0O0OO0OO00O :O0000OO0OO0OOOO00 if O0O00O0O0OO0OO00O in 'aeiou'else O0000OO0OO0OOOO00 .upper ()if O0O00O0O0OO0OO00O in 'AEIOU'else O0O00O0O0OO0OO00O ,OOO00OO0O0O0OO000 .text )#line:42
    print (''.join (O0O00OOO00OOO00OO ))#line:44
if __name__ =='__main__':#line:48
    main ()#line:49
