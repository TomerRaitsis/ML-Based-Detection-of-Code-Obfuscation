import requests #line:1
import tkinter as tk #line:2
def get_random_quote ():#line:6
    try :#line:7
        O00O0OOO0000OOOO0 =requests .get ("https://api.quotable.io/random")#line:8
        O0O0O0O00O0O00OO0 =O00O0OOO0000OOOO0 .json ()#line:9
        O00O000OO0O0O0O0O =O0O0O0O00O0O00OO0 ["content"]#line:10
        O0O00O00O000OOOO0 =O0O0O0O00O0O00OO0 ["author"]#line:11
        quote_text .set (f'"{O00O000OO0O0O0O0O}" - {O0O00O00O000OOOO0}')#line:12
    except requests .exceptions .RequestException as OOO00OOO0OOOO000O :#line:13
        quote_text .set ("Failed to fetch a quote. Check your internet connection.")#line:14
root =tk .Tk ()#line:18
root .title ("Random Quote Generator")#line:19
quote_text =tk .StringVar ()#line:22
quote_label =tk .Label (root ,textvariable =quote_text ,wraplength =300 ,font =("Helvetica",12 ))#line:25
quote_label .pack (pady =20 )#line:26
new_quote_button =tk .Button (root ,text ="Get a New Quote",command =get_random_quote )#line:29
new_quote_button .pack ()#line:30
get_random_quote ()#line:33
root .mainloop ()#line:36
