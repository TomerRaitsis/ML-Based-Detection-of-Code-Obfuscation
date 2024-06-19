import random #line:1
import math #line:2
alpha ="abcdefghijklmnopqrstuvwxyz"#line:4
num ="0123456789"#line:5
special ="@#$%&*"#line:6
pass_len =int (input ("Enter Password Length"))#line:9
alpha_len =pass_len //2 #line:12
num_len =math .ceil (pass_len *30 /100 )#line:13
special_len =pass_len -(alpha_len +num_len )#line:14
password =[]#line:17
def generate_pass (O0OOO00O0O000O0OO ,O000O0O0OO0O0OOOO ,is_alpha =False ):#line:20
    for O0000OO0OOOOOO000 in range (O0OOO00O0O000O0OO ):#line:21
        OO0OO00OO0O00000O =random .randint (0 ,len (O000O0O0OO0O0OOOO )-1 )#line:22
        O0O0O00O00O00O00O =O000O0O0OO0O0OOOO [OO0OO00OO0O00000O ]#line:23
        if is_alpha :#line:24
            O0OO00OOO00OOO00O =random .randint (0 ,1 )#line:25
            if O0OO00OOO00OOO00O ==1 :#line:26
                O0O0O00O00O00O00O =O0O0O00O00O00O00O .upper ()#line:27
        password .append (O0O0O00O00O00O00O )#line:28
generate_pass (alpha_len ,alpha ,True )#line:32
generate_pass (num_len ,num )#line:34
generate_pass (special_len ,special )#line:36
random .shuffle (password )#line:38
gen_password =""#line:40
for i in password :#line:41
    gen_password =gen_password +str (i )#line:42
print (gen_password )#line:43
