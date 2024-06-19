#!/usr/bin/env python3
""#line:2
import argparse #line:4
import os #line:5
import random #line:6
def get_args ():#line:10
    ""#line:11
    OO00000O0OOOOOO0O =argparse .ArgumentParser (description ='Ransom Note',formatter_class =argparse .ArgumentDefaultsHelpFormatter )#line:15
    OO00000O0OOOOOO0O .add_argument ('text',metavar ='text',help ='Input text or file')#line:17
    OO00000O0OOOOOO0O .add_argument ('-s','--seed',help ='Random seed',metavar ='int',type =int ,default =None )#line:24
    OO0O00O0OOOO0O0OO =OO00000O0OOOOOO0O .parse_args ()#line:26
    if os .path .isfile (OO0O00O0OOOO0O0OO .text ):#line:28
        OO0O00O0OOOO0O0OO .text =open (OO0O00O0OOOO0O0OO .text ).read ().rstrip ()#line:29
    return OO0O00O0OOOO0O0OO #line:31
def main ():#line:35
    ""#line:36
    OO00O000OO0000O00 =get_args ()#line:38
    random .seed (OO00O000OO0000O00 .seed )#line:39
    print (''.join ([choose (OOOO00OOOO0O00OO0 )for OOOO00OOOO0O00OO0 in OO00O000OO0000O00 .text ]))#line:42
def choose (O00OO000OO0OO0OO0 ):#line:46
    ""#line:47
    return O00OO000OO0OO0OO0 .upper ()if random .choice ([0 ,1 ])else O00OO000OO0OO0OO0 .lower ()#line:49
def test_choose ():#line:53
    ""#line:54
    O0OO0O00O00000OOO =random .getstate ()#line:56
    random .seed (1 )#line:57
    assert choose ('a')=='a'#line:58
    assert choose ('b')=='b'#line:59
    assert choose ('c')=='C'#line:60
    assert choose ('d')=='d'#line:61
    random .setstate (O0OO0O00O00000OOO )#line:62
if __name__ =='__main__':#line:66
    main ()#line:67
