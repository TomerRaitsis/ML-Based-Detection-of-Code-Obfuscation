from sumeval .metrics .rouge import RougeCalculator #line:5
from sumeval .metrics .bleu import BLEUCalculator #line:6
def eval_rouges (OOO00OO0000OOO0O0 ,OO0OO00OO0OO0O0O0 ):#line:9
    O00OOO0OOO00O0O00 =RougeCalculator (stopwords =True ,lang ="en")#line:13
    O0000O0O000O00O00 =O00OOO0OOO00O0O00 .rouge_n (summary =OO0OO00OO0OO0O0O0 ,references =OOO00OO0000OOO0O0 ,n =1 )#line:18
    O0OOO0OO0OO0OOOOO =O00OOO0OOO00O0O00 .rouge_n (summary =OO0OO00OO0OO0O0O0 ,references =[OOO00OO0000OOO0O0 ],n =2 )#line:23
    OOOO00OO0O000OOO0 =O00OOO0OOO00O0O00 .rouge_l (summary =OO0OO00OO0OO0O0O0 ,references =[OOO00OO0000OOO0O0 ])#line:27
    O0OOOO0O0OO0OO0OO =O00OOO0OOO00O0O00 .rouge_be (summary =OO0OO00OO0OO0O0O0 ,references =[OOO00OO0000OOO0O0 ])#line:33
    O0O00OOO00000000O =BLEUCalculator ()#line:35
    OOOO0O0OOOOO000O0 =O0O00OOO00000000O .bleu (summary =OO0OO00OO0OO0O0O0 ,references =[OOO00OO0000OOO0O0 ])#line:37
    return O0000O0O000O00O00 ,O0OOO0OO0OO0OOOOO ,OOOO00OO0O000OOO0 ,O0OOOO0O0OO0OO0OO ,OOOO0O0OOOOO000O0 #line:43
