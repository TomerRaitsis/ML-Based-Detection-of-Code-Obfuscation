import mysql.connector as c

con = c.connect(host="localhost", user="root", password="password@123")
cur = con.cursor()
cur.execute("use password_manager")


# to perform the modulus operation
def mod(num):
    if num < 0:
        result = 26 - (abs(num) % 26)
    else:
        result = num % 26
    return result
import mysql .connector as c #line:1
con =c .connect (host ="localhost",user ="root",password ="password@123")#line:3
cur =con .cursor ()#line:4
cur .execute ("use password_manager")#line:5
def mod (OO00000OO0O00O0OO ):#line:9
    if OO00000OO0O00O0OO <0 :#line:10
        O000OOO00O0000O0O =26 -(abs (OO00000OO0O00O0OO )%26 )#line:11
    else :#line:12
        O000OOO00O0000O0O =OO00000OO0O00O0OO %26 #line:13
    return O000OOO00O0000O0O #line:14
def hill_cipher (O0OO0OO00O00OO0O0 ,O0O00OOOOO000OOO0 ):#line:17
    OO00OO0OO000O00OO =[]#line:18
    OO0O0O0000000OOOO =0 #line:19
    for O00O0OO0O0OO0O00O in range (3 ):#line:20
        OO0O0O0000000OOOO +=(O0OO0OO00O00OO0O0 [O00O0OO0O0OO0O00O ]-1 )*O0O00OOOOO000OOO0 [O00O0OO0O0OO0O00O ]#line:21
    OO00OO0OO000O00OO .append (OO0O0O0000000OOOO )#line:22
    OO0O0O0000000OOOO =0 #line:24
    for O00O0OO0O0OO0O00O in range (3 ,6 ):#line:25
        OO0O0O0000000OOOO +=(O0OO0OO00O00OO0O0 [O00O0OO0O0OO0O00O -3 ]-1 )*O0O00OOOOO000OOO0 [O00O0OO0O0OO0O00O ]#line:26
    OO00OO0OO000O00OO .append (OO0O0O0000000OOOO )#line:27
    OO0O0O0000000OOOO =0 #line:29
    for O00O0OO0O0OO0O00O in range (6 ,9 ):#line:30
        OO0O0O0000000OOOO +=(O0OO0OO00O00OO0O0 [O00O0OO0O0OO0O00O -6 ]-1 )*O0O00OOOOO000OOO0 [O00O0OO0O0OO0O00O ]#line:31
    OO00OO0OO000O00OO .append (OO0O0O0000000OOOO )#line:32
    return OO00OO0OO000O00OO #line:33
def message (O00000OOOOO00O00O ):#line:36
    O00OO00O0O0OOO0OO =" "#line:37
    O0O00O0OOO00OO0O0 =[]#line:38
    O0OOO00OOO000O00O =[]#line:39
    for O000OOOO0OO000OOO in range (3 ):#line:40
        O0O00O0OOO00OO0O0 .append (O00000OOOOO00O00O [O000OOOO0OO000OOO ])#line:41
    for O000OOOO0OO000OOO in range (3 ):#line:42
        cur .execute (f"select lid from loalpha where lchar = '{O0O00O0OOO00OO0O0[O000OOOO0OO000OOO]}'")#line:43
        O000000O00O0O0OO0 =cur .fetchone ()#line:44
        for O000OOOO0OO000OOO in O000000O00O0O0OO0 :#line:45
            O0OOO00OOO000O00O .append (O000OOOO0OO000OOO )#line:46
    O000000O00O0O0OO0 =[4 ,15 ,24 ,9 ,17 ,0 ,15 ,6 ,17 ]#line:47
    O0O0000OO0OO0O0O0 =hill_cipher (O0OOO00OOO000O00O ,O000000O00O0O0OO0 )#line:48
    for O000OOOO0OO000OOO in O0O0000OO0OO0O0O0 :#line:50
        OO00O000O0OOO00OO =mod (O000OOOO0OO000OOO )#line:51
        cur .execute (f"select lchar from loalpha where lid = {OO00O000O0OOO00OO + 1}")#line:52
        OO0000OO0O0OO0O0O =cur .fetchone ()#line:53
        O00OO00O0O0OOO0OO +=OO0000OO0O0OO0O0O [0 ]#line:55
    return O00OO00O0O0OOO0OO #line:57
if __name__ =="__main__":#line:60
    a =input ("enter the coded text: ")#line:61
    print (message (a ))#line:62


def hill_cipher(text, key_matrix):
    cipher_text = []
    sum = 0
    for i in range(3):
        sum += (text[i] - 1) * key_matrix[i]
    cipher_text.append(sum)

    sum = 0
    for i in range(3, 6):
        sum += (text[i - 3] - 1) * key_matrix[i]
    cipher_text.append(sum)

    sum = 0
    for i in range(6, 9):
        sum += (text[i - 6] - 1) * key_matrix[i]
    cipher_text.append(sum)
    return cipher_text


def message(actual_text):
    HillCipherText = " "
    sect = []
    matrix = []
    for i in range(3):
        sect.append(actual_text[i])
    for i in range(3):
        cur.execute(f"select lid from loalpha where lchar = '{sect[i]}'")
        l = cur.fetchone()
        for i in l:
            matrix.append(i)
    l = [4, 15, 24, 9, 17, 0, 15, 6, 17]
    h = hill_cipher(matrix, l)

    for i in h:
        r = mod(i)
        cur.execute(f"select lchar from loalpha where lid = {r + 1}")
        t = cur.fetchone()

        HillCipherText += t[0]

    return HillCipherText


if __name__ == "__main__":
    a = input("enter the coded text: ")
    print(message(a))
