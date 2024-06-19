import os #line:1
from PIL import Image ,ImageDraw ,ImageFont #line:4
def make_cards (OO0OOO00OO0O00OOO ):#line:7
    ""#line:13
    os .makedirs ("imageCards",exist_ok =True )#line:15
    OOOOO0OOOO0OO0000 =Image .open ("flower.png")#line:18
    with open (OO0OOO00OO0O00OOO )as O0OOOO000OOO0O00O :#line:21
        for OO00OO0OO00000000 in O0OOOO000OOO0O00O :#line:22
            O000O000OOOOO0000 =OO00OO0OO00000000 [:-1 ]#line:23
            O0O0O00O0OOOOO00O =Image .new ("RGBA",(288 ,360 ),"white")#line:26
            O0O0O00O0OOOOO00O .paste (OOOOO0OOOO0OO0000 ,(0 ,0 ))#line:28
            OO00OOOOO00O0000O =Image .new ("RGBA",(291 ,363 ),"black")#line:31
            OO00OOOOO00O0000O .paste (O0O0O00O0OOOOO00O ,(3 ,3 ))#line:32
            OOOO00OO0OOOOOO0O =ImageDraw .Draw (OO00OOOOO00O0000O )#line:35
            O0OO0O0O0000OOOOO =ImageFont .truetype ("Pacifico.ttf",24 )#line:36
            OOOO00OO0OOOOOO0O .text ((120 ,100 ),O000O000OOOOO0000 ,fill ="red",font =O0OO0O0O0000OOOOO )#line:37
            OO00OO00OOO00O0OO ="{}_card.png".format (O000O000OOOOO0000 )#line:40
            OO00OOOOO00O0000O .save (os .path .join ("imageCards",OO00OO00OOO00O0OO ))#line:41
if __name__ =="__main__":#line:44
    make_cards ("guests.txt")#line:45
