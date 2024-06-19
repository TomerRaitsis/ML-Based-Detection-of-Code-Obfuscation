#!/usr/bin/env python3
""#line:2
import argparse #line:4
import os #line:5
import random #line:6
def get_args ():#line:10
    ""#line:11
    OO0O000O0OO0000O0 =argparse .ArgumentParser (description ='Ransom Note',formatter_class =argparse .ArgumentDefaultsHelpFormatter )#line:15
    OO0O000O0OO0000O0 .add_argument ('text',metavar ='text',help ='Input text or file')#line:17
    OO0O000O0OO0000O0 .add_argument ('-s','--seed',help ='Random seed',metavar ='int',type =int ,default =None )#line:24
    O00OOOO0O000OOO00 =OO0O000O0OO0000O0 .parse_args ()#line:26
    if os .path .isfile (O00OOOO0O000OOO00 .text ):#line:28
        O00OOOO0O000OOO00 .text =open (O00OOOO0O000OOO00 .text ).read ().rstrip ()#line:29
    return O00OOOO0O000OOO00 #line:31
def main ():#line:35
    ""#line:36
    O0O0O000O0O000O00 =get_args ()#line:38
    random .seed (O0O0O000O0O000O00 .seed )#line:39
    O0OOOO0O000O0O0OO =map (choose ,O0O0O000O0O000O00 .text )#line:42
    print (''.join (O0OOOO0O000O0O0OO ))#line:43
def choose (O0000000OO00OO000 ):#line:47
    ""#line:48
    return O0000000OO00OO000 .upper ()if random .choice ([0 ,1 ])else O0000000OO00OO000 .lower ()#line:50
def test_choose ():#line:54
    ""#line:55
    OOOO0OOO000O00OOO =random .getstate ()#line:57
    random .seed (1 )#line:58
    assert choose ('a')=='a'#line:59
    assert choose ('b')=='b'#line:60
    assert choose ('c')=='C'#line:61
    assert choose ('d')=='d'#line:62
    random .setstate (OOOO0OOO000O00OOO )#line:63
if __name__ =='__main__':#line:67
    main ()#line:68
