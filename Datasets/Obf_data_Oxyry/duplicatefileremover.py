import hashlib #line:1
import os #line:2
def hashFile (OOOOOOO0000OO0O00 ):#line:7
    OOOOOO000OOOOO000 =65536 #line:9
    O00000OO0O0O0OOOO =hashlib .md5 ()#line:10
    with open (OOOOOOO0000OO0O00 ,'rb')as OOOO0OOOOOO000000 :#line:11
        OO0OOO0OOO00O0000 =OOOO0OOOOOO000000 .read (OOOOOO000OOOOO000 )#line:13
        while (len (OO0OOO0OOO00O0000 )>0 ):#line:14
            O00000OO0O0O0OOOO .update (OO0OOO0OOO00O0000 )#line:15
            OO0OOO0OOO00O0000 =OOOO0OOOOOO000000 .read (OOOOOO000OOOOO000 )#line:16
    return O00000OO0O0O0OOOO .hexdigest ()#line:17
if __name__ =="__main__":#line:20
    hashMap ={}#line:22
    deletedFiles =[]#line:25
    filelist =[O00OO00000OOO0000 for O00OO00000OOO0000 in os .listdir ()if os .path .isfile (O00OO00000OOO0000 )]#line:26
    for f in filelist :#line:27
        key =hashFile (f )#line:28
        if key in hashMap .keys ():#line:30
            deletedFiles .append (f )#line:31
            os .remove (f )#line:32
        else :#line:33
            hashMap [key ]=f #line:34
    if len (deletedFiles )!=0 :#line:35
        print ('Deleted Files')#line:36
        for i in deletedFiles :#line:37
            print (i )#line:38
    else :#line:39
        print ('No duplicate files found')#line:40
