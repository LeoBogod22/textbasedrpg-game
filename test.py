from random import randint


import os

import random

go = True
IsShopLocked = False
IsDaggerEquipped = False
IsSpellBookEquipped=False
IsSwordEquipped = False
IsLeatherHideEquipped = False

IsQuest=False


def dungeon():



    print("you have chosen not to talk to the villager")

    print("you are now continuing your path")

    
def house():

    print("kjldfkj")


def quest():

    print("a Mage has approaced you ")

    print("I think you are now ready to complete the quest")


def profession():
    
    print("**************************************")
    print(" *        What is your class?        *",'\n',
          "*        press f for Fighter         *",'\n',
          "*        press w for warior          *",'\n',
          "*        press m for Mage            *",'\n',
          "*                                    *",'\n',
          "**************************************")
    pclass=input(">>>")
    if pclass =="f":
        Prof = Fighter()
    elif pclass=="w":
        Prof = warior()
    elif pclass == "m":
        Prof = Mage()
    else:
        Prof=Fighter()
        #profession()
    return Prof
hero=profession()


print("name hp thaco ac inventory xp",'\n',
      hero.name,hero.hp,hero.damage,hero.ac,hero.inventory,hero.exp)

hero.hp-=2
print("you",hero.hp)

print("""\


    |>>>                                                      |>>>
    |                     |>>>          |>>>                  |
    *                     |             |                     *
   / \                    *             *                    / \
  /___\                 _/ \           / \_                 /___\
  [   ]                |/   \_________/   \|                [   ]
  [ I ]                /     \       /     \                [ I ]
  [   ]_ _ _          /       \     /       \          _ _ _[   ]
  [   ] U U |        {#########}   {#########}        | U U [   ]
  [   ]====/          \=======/     \=======/          \====[   ]
  [   ]    |           |   I |_ _ _ _| I   |           |    [   ]
  [___]    |_ _ _ _ _ _|     | U U U |     |_ _ _ _ _ _|    [___]
  \===/  I | U U U U U |     |=======|     | U U U U U | I  \===/
   \=/     |===========| I   | + W + |   I |===========|     \=/
    |  I   |           |     |_______|     |           |   I  |
    |      |           |     |||||||||     |           |      |
    |      |           |   I ||vvvvv|| I   |           |      |
_-_-|______|-----------|_____||     ||_____|-----------|______|-_-_
   /________\         /______||     ||______\         /________\
  |__________|-------|________\_____/________|-------|__________|
  """)
print("/n2")
print("/n2")
print("it is a  a sunny day")


print ("where would you like to go next?")

move2=int(input("press 1 for north 2 for east and 3 for west "))


if move2==1:

 print("you have approached a house ")
 print("""\

                  .-.__
                                          (     `-.
                                           [`--.__ )
                                           | ][  ]/
                                          .--.][_|
                                         /        `----.______
                     _.-----------------'                     `---------------.
                   .'                                                          \
                   |                                                            |
                   |                                                            |
                   |                                                            |
                   |                                                            |
                   |                                                            |
                   |                                                            |
                   |                                                            |
                   |                                                            |
                   |                                                            |
                    \                                                           |
                     `-._______________                  _.-------._            |
                      | |              `-.   .----------'           `.          |
                      | |   _________     \ / __________       _______\         |
                      | |  |   |||   |     Y |/////\\\\\|     |   |||  `.      /
                      | |  |   |||   |     | |/////\\\\\|     |   |||   |`-.__/
                      | |  |____|____|       |/////\\\\\|     |____|____|   | |
  VK                  | |  | ,,,| \  |       |////  \\\\|     |  / | \  |   | |
                      | |  |(o o|  \ |       |///\  /\\\|     | /  |  \ |   | |
                      | |  |____|____|       |////\/\\\\|     |____|____|   | |
`-------._______      | |  |/   |,,, |       |o==//\\\\\|     | \  |  / |   | |____.---------
                `----.| |__|.---|o o)|       |@////\\\\\|     |  \_|__.------'
               _.------'          `--+------.|/////\\\\\|_.---+--'
----.___.-----'                                                                _________.----
                             _.------------.________________.-----------------' o
                                        """)
 p=int(input(" a sword is on the floor press 1 to pick it up "))

 
hero.inventory.update({"sword"
                       })
hero.damage+=10
print("your inventroy is" ,hero.inventory)
print("your attack damage is" ,hero.damage)




if move2==2:

    print("the sun is shinging bright")
    print("you have found 15 gold on the floor")
    hero.ac+=15

    print(" you now have " ,hero.ac, "gold")





print("where would you like to go ?")


move=int(input("press 1 to go  north 2 to go  east and 3 to go  west"))



if move==1:

 print("your moving north the sun is shining you way")



elif move==2:

 print("you have approached an old house")
 print("========**")
 print("====*******")



elif move ==3:




 

      

 print("you see a town archmage walking by")

movee=int(input("press 1 talk to him  2 to pass"))


if movee==2:

 print("you have approached an old house")
 dungeon()



elif movee==1:

 print("I have a quest for you. The grim reaper of death has been tormenting our village")
 print("-----------------")
print("-----------------")
print("we need to stop him")
print("-----------------")
print("-----------------")
print("he comes out at night. Please help us and kill him")
movede=int(input("press 1 to accept the quest"))

 







def fight(drag):
 while hero.hp>=0 and drag.hp>=0:
 
                                        





  dmgg=randint(0,hero.damage)

mana=20
       
print("""                                  .""--..__
                     _                     []       ``-.._
                  .'` `'.                  ||__           `-._
                 /    ,-.\                 ||_ ```---..__     `-.
                /    /:::\\               /|//}          ``--._  `.
                |    |:::||              |////}                `-. \
                |    |:::||             //'///                    `.\
                |    |:::||            //  ||'                      `|
           /    |:::|/        _,-//\  ||
               /`    |:::|`-,__,-'`  |/  \ ||
             /`  |   |'' ||           \   |||
           /`    \   |   ||            |  /||
         |`       |  |   |)            \ | ||
        |          \ |   /      ,.__    \| ||
        /           `         /`    `\   | ||
       |                     /        \  / ||
       |                     |        | /  ||
       /         /           |        `(   ||
      /          .           /          )  ||
     |            \          |     ________||
    /             |          /     `-------.|
   |\            /          |              ||
   \/`-._       |           /              ||
    //   `.    /`           |              ||
   //`.    `. |             \              ||
  ///\ `-._  )/             |              ||
 //// )   .(/               |              ||
 ||||   ,'` )               /              //
 ||||  /                    /             || 
 `\\` /`                    |             // 
     |`                     \            ||  
    /                        |           //  
  /`                          \         //   
/`                            |        ||    
`-.___,-.      .-.        ___,'        (/    
         `---'`   `'----'`  """)

                                     
                       
   
print(drag.name , "is attacking the villager")
m=int(input("press 1 to continue"))
print("================================")

print("""                   .-----.
                         .'       `.
                        :      ^v^  :
                        :           :
                        '           '
         |~        www   `.       .'
        /.\       /#^^\_   `-/\--'
       /#  \     /#%    \   /# \
      /#%   \   /#%______\ /#%__\
     /#%     \   |= I I ||  |- | ===
     ~~|~~~|~~   |_=_-__|'  |[]|
       |[] |_______\__|/_ _ |= |`.
^V^    |-  /= __   __    /-\|= | :;
       |= /- /\/  /\/   /=- \.-' :;  'v'
       | /_.=========._/_.-._\  .:'
       |= |-.'.- .'.- |  /|\ |.:'
       \  |=|:|= |:| =| |~|~||'|
        |~|-|:| -|:|  |-|~|~||=|      ^V^
        |=|=|:|- |:|- | |~|~|| |
        | |-_~__=_~__=|_^^^^^|/___
        |-(=-=-=-=-=-(|=====/=_-=/\
        | |=_-= _=- _=| -_=/=_-_/__\ 
        | |- _ =_-  _-|=_- |]#| I II
        |=|_/ \_-_= - |- = |]#| I II
        | /  _/ \. -_=| =__|]!!!I_II!!
       _|/-'/  ` \_/ \|/' _ ^^^^`.==_^.
     _/  _/`-./`-; `-.\_ / \_'\`. `. ===`.
    / .-'  __/_   `.   _/.' .-' `-. ; ====;\
   /.   `./    \ `. \ / -  /  .-'.' ====='  >
  /  \  /  .-' `--.  / .' /  `-.' ======.' / """)
print("its up to you to save him")
print("your inventory is " , hero.inventory,)

print ("your attack damage is " ,hero.damage,)
spell = int(input("press 1 for fireball , 2 for malethic curse 3 for basic attack"))

if spell==1:
 drag.hp-=10
 mana=-2
print("dragon has",drag.hp,"left")

print("dragon has attacked you  with a roar of flame")
print("")
hero.hp-=randint(0,20)
print("you have" ,hero.hp, "left")



print("you have attacked dragon and did 7 damage ")
             
drag.hp-=7
print("dragon has", drag.hp ,"left")

if spell==2:

            drag.hp-=20
            print("Repear has", drag.hp ,"left")

            print("repear has attacked you ")
            hero.hp-=randint(0,20)
            print("you have" ,hero.hp, "left")
          

print("you have attacked repearand did 10 damage")
             
drag.hp-=10
print("repear has", drag.hp ,"left")

            
if spell==3:
 drag.hp-=13
 print(drag.hp)

print("repear has attacked you ")
hero.hp-=randint(0,20)
print("you have" ,hero.hp, "left")


print("you have attacked repear and did 15 damage ")
             
drag.hp-=15
print("repear has", drag.hp ," health left")

if drag.hp==0:

    hero.exp+=10

hero.ac+=5
print("you have slain repear and gained 10 xp")

print ("you now have " ,hero.exp , "and " ,hero.ac," gold")



print("quest is completed")

IsQuest=True



def villager():


  

    response=["hi would you like to complete a quest?", " there is a giant orc in the dungeon " ,"i m looking for treasure",]

    print(random.choice(response))


    move2=input("would you like to help me? Y/N ")


    if move2=="Y":

     print("thankyou ")
    quest()


    if move2 =="N":


     main()


           
def read():

 print("you are ready for q quest")
        
 quest()
def main():
        print("you have approached  a small building")
        print("""/                            +&-
                          _.-^-._    .--.
                       .-'   _   '-. |__|
                      /     |_|     \|  |
                     /               \  |
                    /|     _____     |\ |
                     |    |==|==|    |  |
 |---|---|---|---|---|    |--|--|    |  |
 |---|---|---|---|---|    |==|==|    |  |
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^""")

        print ("where would you like to go next?")

move2=int(input("press 1 to enter the house 2 to go  east and 3 for west "))


if move2==1:

 house()




 if move2==2:


    print("you haveapproached a shop")

shop()



if move2==3:

    print("you are now outside in the village of larkville")
    read()




print("where would you like to go ?")


move=int(input("press 1 to go  north 2 to go  east and 3 to go  west"))



if move==1:

 print("your moving north the sun is shining you way")



elif move==2:

 print("you have approached a fountain")
 print("========**")
 print("====*******")
     



elif move ==3:



 print("walking north")
 

      
print (" a villager is walking by")
num=int(input("would yo like to talk to him press 2 to talk. 1 to pass "))

if num==2:


 villager()


elif num==1:

  print("you are walking forwared")
