
import random
import time
key=False
spider=False
snake=False
tea=False
life=20
done=False
unlock=False
win=False
weapon=0
ch6=False
been7=False
been12=False
def fight(monster,mname):
    global weapon, life,attack,done
    while life>0 and monster>0:
        playerp=random.randint(1,5)+attack
        monsterp=random.randint(1,5)
        if playerp>monsterp:
            print("You hit the",mname,"!")
            monster=monster-3
        elif playerp<monsterp:
            print("The",mname,"attacks you!")
            life=life-3
        else:
            print("You collide into each other...neither of you score a hit")
    if life<=0:
        print("You die in severe agony")
        done=True
    elif monster<=0:
        print("You defeat the",mname,"!")
        win = True
        return win
def equip(points,wname):
    global weapon
    print ("It could be useful for fighting monsters")
    if weapon!=0:
            print("Equip the",wname,"? (y) or (n)\n(You will have to give up your current weapon)")
            equip=input()
    else:
           print("Equip the",wname,"? (y) or (n)")
           equip= input()
    while equip.upper()!="Y" and equip.upper()!="N":
        equip= input("Invalid selection\nPlease type (y) or (n)\n")
    if equip.upper()=="Y":
        print("You equip the",wname)
        print("It gives you",points,"extra hit points")
        weapon=points
        chosen=True
        return chosen
    if equip.upper()=="N":
        print("You don't equip the",wname)
        chosen=False
        chosen=False
def droom0():
    print("You are in the foyer of the mansion")
        
def droom1():
    global key
    print("You are in the library of the mansion")
    if not key and next_room!=None:
        if next_room!=3 or key==True:
            print("You find a key on the bookshelf\nDo you want to take it\n(Y or N)")
        take=input()
        while take.upper()!="Y" and take.upper()!="N":
            print("Please type Y or N")
            take=input()
        if take.upper()=="Y":
            print("You take the key")
            key=True
        else:
            print("You don't take the key")
            
def droom2():
    global spider
    global life
    print("You are in the kitchen of the mansion")
    if not spider and next_room!=None:
        if next_room!=3 or key==True:
            print("You find a spider in the corner\nFight it?\n(Y or N)")
            fight=input()
            
            
            while fight.upper()!="Y" and fight.upper()!="N":
                print("Please type Y or N")
                fight=input()
                
            if fight.upper()=="Y":
                print("You fight the spider")
                win=random.randint(0, 2)
                
                if win==0 or win==2:
                    print("You lose the fight, the spider injures you")
                    life -=2
                    print("You have:", life, "life points left")
                if win==1:
                    print("You kill the spider")
                    spider=True
            else:
                print("You run past the spider, but it bites you")
                life-=1
                print("You have:", life, "life points left")

def droom3():
    print("You are in the bedroom of the mansion")
    print("Inside the bedroom, there is a tunnel for escape")
    print("You exit the mansion to your freedom")
    print("CONGRATULATIONS\nYOU WIN!")

def droom4():
    print("You stand in a corridor\nThere is a painting of a man on the wall\nHe looks familiar")
def droom5():
    print("You stand in a corridor\nThere are some dead flowers across the flower")
def droom6():
    global ch6
    print ("You are in the dining hall of the mansion")
    if not ch6:
        print ("There is no food here but you do find a big spoon")
        ch6=equip(3,"spoon")
    else:
        print("The tables are empty, not even a table cloth")
    print("A narrow set of stairs wind down towards the north")
    
def droom7():
    global life
    print("You are in the ball room")
    if not been7:
        print("It's quite dusty")
        print("You cough a bit and lose 1 health")
        life-=1
        bee7=True
    else:
        print("You remember that it's dusty and hold your breath")
    print("There is nothing much to see here\nNo balls")
    print("A narrow set of stairs wind up towards the north")
        
def droom8():
    print()
def droom9():
    global tea
    global life
    print("You are in the maid's quarters\nThere are no maids")
    if not tea and next_room!=None:
        if next_room!=3 or tea==True:
            print("You find a cup of tea on the desk\nDo you want to drink it\n(Y or N)")
        take=input()
        while take.upper()!="Y" and take.upper()!="N":
            print("Please type Y or N")
            take=input()
        if take.upper()=="Y":
            print("You drink the tea")
            tea=True
            print("Your life point increases by 3")
            life+=3
            print("You have:", life, "life points left")
        else:
            print("You don't drink the tea")
def droom10():
    print()
def droom11():
    global snake
    global life
    print("You are in the garden")
    if not spider and next_room!=None:
        if next_room!=3 or key==True:
            print("You find a snake under the bushes\nFight it?\n(Y or N)")
            fight=input()
            
            
            while fight.upper()!="Y" and fight.upper()!="N":
                print("Please type Y or N")
                fight=input()
                
            if fight.upper()=="Y":
                print("You fight the snake")
                win=random.randint(0, 3)
                
                if win==0 or win==2 or win==3:
                    print("You lose the fight, the snake poisons you")
                    life -=2
                    print("You have:", life, "life points left")
                if win==1:
                    print("You kill the snake")
                    snake=True
            else:
                print("You run past the snake, but it bites you")
                life-=1
                print("You have:", life, "life points left")
def droom12():
    global been12
    if been12==False:
        print("You're in the cellar of the mansion")
        time.sleep(1)
        print("There is no alcohol... but there is something in the room dimly lit by the candle")
        time.sleep(1)
        print("Who lit the candle?")
        print("You run")
        been12=True
    else:
        print("You come back to the dimly lit cellar")
        print("Whatever the thing was, it's still there")
        print("You decide to go closer")
        print("To your horror, it's a woman...with gashes all over her body")
        print("She screams in agony and jumps towards you")
        woman=fight(15,"woman")
    
def droom13():
    global been13
    print("You're in the attic of the mansion")
room0 = ["droom0()",1,3,None,None]
room1 = ["droom1()",4,2,0,None]
room2 = ["droom2()",5,None,3,1]
room3 = ["droom3()",2,None,None,0]
room4 = ["droom4()",6,9,1,5]
room5 = ["droom5()",7,4,2,11]
room6 = ["droom6()",12,8,4,7]
room7 = ["droom7()",13,6,5,10]
room8 = ["droom8()",None,None,9,6]
room9 = ["droom9()",8,None,None,4]
room10 = ["droom10()",None,7,11,None]
room11 = ["droom11()",10,5,None,None]
room12 = ["droom12()",None,None,6,None]
room13 = ["droom13()",None,None,7,None]
room_list=[room0,room1,room2,room3,room4,room5,room6,room7,room8,room9,room10,room11,room12,room13]
current_room=0



print("\n\n\n...after what seems like an eternity, you slowly open your eyes to the eerie scene\nyou find yourself in an ancient mansion that has long since been abandoned\nyou get up and start to walk around")
while not done:
    global done
    print("\n---------------------------------------------------\n")
    global unlock
    
    exec(room_list[current_room][0])
    if life<=0:
        print("You die in severe agony")
        print("Game over")
        done=True
        break
    print("You have",life,"life points left")
    print("█"*life,end='')
    blank=30-life
    print("▄"*blank,"\n")
    
    v= input("Where to go? Select N, E, S or W\n")
    if v.upper()=="N":
        next_room=room_list[current_room][1]
        if next_room==3 and key==False:
            print("\nThe bedroom is locked, try to find the key\n")
        elif next_room==3 and key==True and unlock==False:
            print("\nYou use the key to unlock the bedroom\n")
            unlock=True
            current_room=next_room
        else:
            print()
        if next_room ==None:
            print("\nYou can't go that way, choose again\n")
        else:
            current_room=next_room
   
   
    elif v.upper()=="E":
        next_room=room_list[current_room][2]
        if next_room==3 and key==False:
            print("\nThe bedroom is locked, try to find the key\n")        
        elif next_room==3 and key==True and unlock==False:
            print("\nYou use the key to unlock the bedroom\n")
            unlock=True
            current_room=next_room
        elif next_room ==None:
            print("\nYou can't go that way, choose again\n")
        else:
            current_room=next_room    
    
   
    elif v.upper()=="S":
        next_room=room_list[current_room][3]
        if next_room==3 and key==False:
            print("\nThe bedroom is locked, try to find the key\n")        
        elif next_room==3 and key==True and unlock==False:
            print("\nYou use the key to unlock the bedroom\n")
            unlock=True
            current_room=next_room        
        elif next_room ==None:
            print("\nYou can't go that way, choose again\n")
        else:
            current_room=next_room   
    
    
    elif v.upper()=="W":
        next_room=room_list[current_room][4]
        if next_room==3 and key==False:
            print("\nThe bedroom is locked, try to find the key\n")        
        elif next_room==3 and key==True and unlock==False:
            print("\nYou use the key to unlock the bedroom\n")
            unlock=True
            current_room=next_room        
        elif next_room ==None:
            print("\nYou can't go that way, choose again\n")
        else:
            current_room=next_room            
    
  
    else:
        print("Invalid selection, try again")
    