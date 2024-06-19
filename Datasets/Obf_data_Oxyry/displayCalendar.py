def display_cal (O0000OOO000OO00O0 ,O0OO000000OO00O0O ):#line:1
    ""#line:9
    import calendar #line:10
    print (calendar .month (O0000OOO000OO00O0 ,O0OO000000OO00O0O ))#line:12
def fetch_year ():#line:15
    ""#line:18
    while True :#line:19
        try :#line:20
            O0OO0OO0O000O0000 =int (input ("Enter year: "))#line:21
            if O0OO0OO0O000O0000 <0 :#line:22
                raise ValueError ("Year must be a positive integer")#line:23
            return O0OO0OO0O000O0000 #line:24
        except ValueError :#line:25
            print ("Invalid input. Please enter a valid year.")#line:26
def fetch_month ():#line:29
    ""#line:32
    while True :#line:33
        try :#line:34
            OO000O00OOO0O00OO =int (input ("Enter month: "))#line:35
            if OO000O00OOO0O00OO <1 or OO000O00OOO0O00OO >12 :#line:36
                raise ValueError ("Month must be between 1 and 12")#line:37
            return OO000O00OOO0O00OO #line:38
        except ValueError :#line:39
            print ("Invalid input. Please enter a valid month.")#line:40
year_input =fetch_year ()#line:43
month_input =fetch_month ()#line:44
display_cal (year_input ,month_input )#line:46
