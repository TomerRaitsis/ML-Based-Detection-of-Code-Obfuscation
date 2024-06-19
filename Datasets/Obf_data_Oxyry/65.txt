import time #line:1
from calendar import isleap #line:2
def judge_leap_year (O00O0OOOO00OO00O0 ):#line:3
    if isleap (O00O0OOOO00OO00O0 ):#line:4
        return True #line:5
    else :#line:6
        return False #line:7
def month_days (OOO0O000O000OO0OO ,O0O0OO0O0OOO0O0O0 ):#line:8
    if OOO0O000O000OO0OO in [1 ,3 ,5 ,7 ,8 ,10 ,12 ]:#line:9
        return 31 #line:10
    elif OOO0O000O000OO0OO in [4 ,6 ,9 ,11 ]:#line:11
        return 30 #line:12
    elif OOO0O000O000OO0OO ==2 and O0O0OO0O0OOO0O0O0 :#line:13
        return 29 #line:14
    elif OOO0O000O000OO0OO ==2 and (not O0O0OO0O0OOO0O0O0 ):#line:15
        return 28 #line:16
name =input ("input your name: ")#line:17
age =input ("input your age: ")#line:18
localtime =time .localtime (time .time ())#line:19
year =int (age )#line:20
month =year *12 +localtime .tm_mon #line:21
day =0 #line:22
begin_year =int (localtime .tm_year )-year #line:23
end_year =begin_year +year #line:24
for y in range (begin_year ,end_year ):#line:25
    if (judge_leap_year (y )):#line:26
        day =day +366 #line:27
    else :#line:28
        day =day +365 #line:29
leap_year =judge_leap_year (localtime .tm_year )#line:30
for m in range (1 ,localtime .tm_mon ):#line:31
    day =day +month_days (m ,leap_year )#line:32
day =day +localtime .tm_mday #line:33
print ("%s's age is %d years or "%(name ,year ),end ="")#line:34
print ("%d months or %d days"%(month ,day ))#line:35
