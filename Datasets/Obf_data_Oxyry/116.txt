import random #line:2
def roll_dice ():#line:5
    print ('\nDo you want to play again ?')#line:6
    print ('Enter Yes/No')#line:7
    O00OO0OOO000OO0OO =input ()#line:8
    if O00OO0OOO000OO0OO =='':#line:11
        print ('Wrong Input !!! Enter again Yes/No')#line:12
        O00OO0OOO000OO0OO =roll_dice ()#line:13
    return O00OO0OOO000OO0OO #line:14
if __name__ =='__main__':#line:16
    print ('Welcome to the Dice Game !!!')#line:17
    dice_value =random .randint (1 ,6 )#line:18
    print ('You got ',dice_value )#line:19
    choice =roll_dice ()#line:20
    while choice :#line:23
        if choice =='No'or choice =='no':#line:24
            break #line:25
        elif choice =='Yes'or choice =='yes':#line:26
            dice_value =random .randint (1 ,6 )#line:27
            print ('You got ',dice_value )#line:28
            choice =roll_dice ()#line:29
        else :#line:30
            print ('Wrong Input !!! Enter again Yes/No')#line:31
            choice =roll_dice ()#line:32
