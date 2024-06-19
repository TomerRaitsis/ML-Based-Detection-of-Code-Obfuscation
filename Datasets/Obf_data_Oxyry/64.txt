from datetime import date #line:1
def ageCalculator (O00OO0OO0000OOOOO ,OOOO000O00O00O0OO ,OO0OOO00OO0O0O000 ):#line:4
    OO0O000OOO0OOO0OO =0 #line:5
    OO0O0OOOO0O000000 =0 #line:6
    OOOO00000OOOO0OO0 =0 #line:7
    OOOOO000O0O0OO0O0 =int (today .strftime ("%d"))#line:9
    O00O00O00OOOO0000 =int (today .strftime ("%m"))#line:10
    O0O0O00OO0OO0000O =int (today .strftime ("%y"))#line:11
    if OOOOO000O0O0OO0O0 <day :#line:13
        OOOOO000O0O0OO0O0 +=31 #line:14
        OO0O000OOO0OOO0OO =OOOOO000O0O0OO0O0 -OO0OOO00OO0O0O000 #line:15
    else :#line:16
        OO0O000OOO0OOO0OO =OOOOO000O0O0OO0O0 -OO0OOO00OO0O0O000 #line:17
    if O00O00O00OOOO0000 <OOOO000O00O00O0OO :#line:19
        O00O00O00OOOO0000 +=12 #line:20
        OO0O0OOOO0O000000 =O00O00O00OOOO0000 -OOOO000O00O00O0OO #line:21
    else :#line:22
        OO0O0OOOO0O000000 =O00O00O00OOOO0000 -OOOO000O00O00O0OO #line:23
    OOOO00000OOOO0OO0 =O0O0O00OO0OO0000O -O00OO0OO0000OOOOO #line:25
    print (f"your age of today is :{O0O0O00OO0OO0000O}-{O00O00O00OOOO0000}-{OOOOO000O0O0OO0O0}")#line:27
today =date .today ()#line:30
print ("today's date is:",today )#line:31
birthDate =input ('Enter your birth date in YYYY-MM-DD format:')#line:32
year ,month ,day =map (int ,birthDate .split ('-'))#line:33
if month >12 or day >31 or year <int (today .strftime ("%y")):#line:34
    print ('invalid date')#line:35
    exit ()#line:36
print ("your date of birth is:",birthDate )#line:37
ageCalculator (year ,month ,day )#line:38
