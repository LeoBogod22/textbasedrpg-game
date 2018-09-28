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

if hero.ac == mage: 
spell = int(input("press 1 for fireball , 2 for malethic curse 3 for basic attack"))


elif hero.ac == warrior: 
spell = int(input("press 1 for cutting blade, 2 stab  3 for basic attack"))


if spell==1:
 drag.hp-=10
 mana=-2
print(drag.name ,drag.hp,"left")

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
print("you have slain , drag.name +  " and gained 10 xp")

print ("you now have " ,hero.exp , "and " ,hero.ac," gold")
