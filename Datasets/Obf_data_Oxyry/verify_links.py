import requests #line:1
import bs4 #line:2
def verify (O0O000OO0OO0O0OOO ):#line:5
    ""#line:11
    OO0O00O00OOO00O0O =requests .get (O0O000OO0OO0O0OOO )#line:13
    try :#line:15
        OO0O00O00OOO00O0O .raise_for_status ()#line:16
        O0OOO000000000000 =bs4 .BeautifulSoup (OO0O00O00OOO00O0O .text ,"html.parser")#line:18
        O0O0OOO00OO00OOOO =[OOOO0OOOO0O00OO0O .get ("href")for OOOO0OOOO0O00OO0O in O0OOO000000000000 .select ("a")if OOOO0OOOO0O00OO0O .get ("href")]#line:19
        OOO00OOO0OOOOO0OO =0 #line:21
        OO0O00O0O00O00O00 =0 #line:22
        for OOO0OOO000OO0OO0O in O0O0OOO00OO00OOOO :#line:24
            if OOO0OOO000OO0OO0O .startswith ("http"):#line:26
                O00O00O00000OOO00 =requests .get (OOO0OOO000OO0OO0O )#line:27
                try :#line:29
                    O00O00O00000OOO00 .raise_for_status ()#line:31
                    print (f"Good: {OOO0OOO000OO0OO0O}")#line:32
                    OO0O00O0O00O00O00 +=1 #line:33
                except Exception as O0OO000OO00OOOOOO :#line:35
                    print (f"Broken: {OOO0OOO000OO0OO0O}")#line:36
                    OOO00OOO0OOOOO0OO +=1 #line:37
        print (f"{OO0O00O0O00O00O00} Good. {OOO00OOO0OOOOO0OO} Broken")#line:39
    except Exception as O0OO000OO00OOOOOO :#line:41
        print ("There was a problem: %s"%(O0OO000OO00OOOOOO ))#line:42
if __name__ =="__main__":#line:45
    verify ("https://automatetheboringstuff.com/chapter11/")#line:46
