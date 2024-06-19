#!/usr/bin/env python3
""#line:2
import argparse #line:4
import os #line:5
import random #line:6
def get_args ():#line:10
    ""#line:11
    OO0000OOO000O0O0O =argparse .ArgumentParser (description ='Ransom Note',formatter_class =argparse .ArgumentDefaultsHelpFormatter )#line:15
    OO0000OOO000O0O0O .add_argument ('text',metavar ='text',help ='Input text or file')#line:17
    OO0000OOO000O0O0O .add_argument ('-s','--seed',help ='Random seed',metavar ='int',type =int ,default =None )#line:24
    OOOO0O0OO0O0OOOOO =OO0000OOO000O0O0O .parse_args ()#line:26
    if os .path .isfile (OOOO0O0OO0O0OOOOO .text ):#line:28
        OOOO0O0OO0O0OOOOO .text =open (OOOO0O0OO0O0OOOOO .text ).read ().rstrip ()#line:29
    return OOOO0O0OO0O0OOOOO #line:31
def main ():#line:35
    ""#line:36
    O0O0O0000000O0O0O =get_args ()#line:38
    random .seed (O0O0O0000000O0O0O .seed )#line:39
    print (''.join (map (choose ,O0O0O0000000O0O0O .text )))#line:42
def choose (OO00O0O00000OOOOO ):#line:46
    ""#line:47
    return OO00O0O00000OOOOO .upper ()if random .choice ([0 ,1 ])else OO00O0O00000OOOOO .lower ()#line:49
def test_choose ():#line:53
    ""#line:54
    OO00OOOO0OO0O0000 =random .getstate ()#line:56
    random .seed (1 )#line:57
    assert choose ('a')=='a'#line:58
    assert choose ('b')=='b'#line:59
    assert choose ('c')=='C'#line:60
    assert choose ('d')=='d'#line:61
    random .setstate (OO00OOOO0OO0O0000 )#line:62
if __name__ =='__main__':#line:66
    main ()#line:67
