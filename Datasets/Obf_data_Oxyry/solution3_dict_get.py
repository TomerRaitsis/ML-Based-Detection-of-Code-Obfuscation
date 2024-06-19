#!/usr/bin/env python3
""#line:2
import argparse #line:4
def get_args ():#line:8
    ""#line:9
    OOOO0000OO0OOO000 =argparse .ArgumentParser (description ='Gashlycrumb',formatter_class =argparse .ArgumentDefaultsHelpFormatter )#line:13
    OOOO0000OO0OOO000 .add_argument ('letter',help ='Letter(s)',metavar ='letter',nargs ='+',type =str )#line:19
    OOOO0000OO0OOO000 .add_argument ('-f','--file',help ='Input file',metavar ='FILE',type =argparse .FileType ('r'),default ='gashlycrumb.txt')#line:26
    return OOOO0000OO0OOO000 .parse_args ()#line:28
def main ():#line:32
    ""#line:33
    O0OOO0000000000OO =get_args ()#line:35
    O00O0OO0O00O00OOO ={OOOO0000O00O00O00 [0 ].upper ():OOOO0000O00O00O00 .rstrip ()for OOOO0000O00O00O00 in O0OOO0000000000OO .file }#line:36
    for OOOO0OOO00OOO0OO0 in O0OOO0000000000OO .letter :#line:38
        print (O00O0OO0O00O00OOO .get (OOOO0OOO00OOO0OO0 .upper (),f'I do not know "{OOOO0OOO00OOO0OO0}".'))#line:39
if __name__ =='__main__':#line:43
    main ()#line:44
