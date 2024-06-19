def displayInventory (OO00OOO00OOOOOO0O ):#line:1
    ""#line:9
    print ("Inventory:")#line:10
    O0OO0OO0O0OO0OOOO =0 #line:11
    for OOO0OOOO0000000O0 ,OO00OOO0O000000OO in OO00OOO00OOOOOO0O .items ():#line:13
        print (OO00OOO0O000000OO ," ",OOO0OOOO0000000O0 )#line:14
        O0OO0OO0O0OO0OOOO +=OO00OOO0O000000OO #line:15
    print ("Total number of items: "+str (O0OO0OO0O0OO0OOOO ))#line:17
def addToInventory (O0OOOO0OO0O0000O0 ,OOOOOO00000O0000O ):#line:20
    ""#line:28
    O0000O0O0000OO00O =dict (O0OOOO0OO0O0000O0 )#line:29
    for OO0OO0OO0000O0O00 in OOOOOO00000O0000O :#line:31
        O0000O0O0000OO00O .setdefault (OO0OO0OO0000O0O00 ,0 )#line:32
        O0000O0O0000OO00O [OO0OO0OO0000O0O00 ]+=1 #line:33
    return O0000O0O0000OO00O #line:35
if __name__ =="__main__":#line:38
    stuff ={"rope":1 ,"torch":6 ,"gold coin":42 ,"dagger":1 ,"arrow":12 }#line:40
    displayInventory (stuff )#line:41
    inv ={"gold coin":42 ,"rope":1 }#line:43
    dragonLoot =["gold coin","dagger","gold coin","gold coin","ruby"]#line:44
    inv =addToInventory (inv ,dragonLoot )#line:45
    displayInventory (inv )#line:46
