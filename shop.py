def shop():

    
    
    spellbook=Item('spellbook',0,15)
    dagger = Item('Dagger', 0, 5)
    sword = Item('Sword', 0, 10)
    leather_hide = Item('Leather Hide', 5, 0)
    if IsShopLocked == True:
        print("The shop is locked!\nPlease go back and continue your adventure!")
    else:
        print("you have passed by a shop")
        print(  """ \
               _ ___ _  _ _   _
                    |\  /||(_  | |_)|_(_  (_
                    | \/ ||__) | | \|___) __)
                    __    _   _ ___      _, _
                   /  |_||_)|(_  | ||\ |(_ (_
                   \__| || \|__) | || \|(_ __)
                   ||    Larkvilles shop     ||
   ________________||_______________________||_____________
  |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_||
  |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|| /|
  |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_||/||
  |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|||/|
  |_|_|_|_|_|_|_|_|_|     _      _     |_|_|_|_|_|_|_|_|_|_|/||
  |_| books  swords |    (_)    (_)    |latex __  leather|_|/||
  |_|.    spells    |__________________|     (^^)  .     |_||/|
  |_|*`.            |_|      ||      |_|     _)(_  I`.   |_|/||
  |_| S `.          |_| llup || push |_|    /()()\/| ;   |_||/|
  |_|`. A `.        |_| tuo  ||  in  |_|   // )_\\/      |_|/||
  |_|  `. L `.      |_|     [||]     |_|   \|.//_)       |_||/|
  |_|    `. E `.    |_|      ||      |_|     // /        |_|/||
  |_|______`__*_`___|_|      ||      |_|_____\\|_________|_||/|
  |_|_|_|_|_|_|_|_|_|_|______||______|_|_|_|_|_|_|_|_|_|_|_|/||
__|_|_|_|_|_|_|_|_|_|_|______||______|_|_|_|_|_|_|_|_|_|_|_||/________
 /     /     /     /     /     /     /     /     /     /     /     /
/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/
___________________________________________________________jro____
 /_/_/_/ """  )
        print("you now have",hero.ac,"gold")
        print("Welcome to the Larkville shop! What would you like to buy?\n1. Weapons\n2. armor\n3. spellbooks and staff 4. exit and complete my quest")
        selection = int(input("Enter a value: "))

    if selection == 1:
        if hero.ac>0:
            print("Weapons shop")
            print("1. Bronze Dagger: $7\n2. Destiny Sword: $50/n2. ")
            wpnselection = int(input("Enter a value: "))

        if wpnselection == 1:
            
            if hero.ac<20:
                print("You dont...")
              
            else:
                dagger = Item('Dagger', 0, 5)
                IsDaggerEquipped = True
                hero.damage+= 34
                hero.ac-=7
                print("/n2")
                print("/n2")
                hero.inventory.update({"bronze Dagger"})
                print("****************")
                print("you Have sussefully bought a Bronze Dagger")
                print("your inventory is ",hero.inventory,)
                print("strength increased to: {}".format(hero.damage))
                print("you have ",hero.ac,"gold left")

        elif wpnselection == 2:
            if hero.ac<50:
                print("You dont have enough gold  yet..")
           
            else:
                sword = Item('Sword', 0, 10)
                IsSwordEquipped = True
                hero.damage +=34
                hero.ac -= 50
                hero.inventory.update({"destiny sword"})
                print("item purchased!")
                print("strength increased to: {}".format(hero.damage))
                print("you have ",hero.ac,"gold left")
                print("your inventory is ",hero.inventory,)
  
    if selection == 2:

            if  hero.ac >0:
              print ("your in the Armor Shop")
            print ("1. Leather hide\n2.Warmorgs Armor (26)")
            armselection = int(input("enter a value: "))

            if armselection == 1:
            
                if hero.ac<34:
                 print("You dont have enoyugh gold!")
              
                else:
                 leather_hide = Item('Leather Hide', 5, 0)
                 IsLeatherHideEquipped = True
                 hero.hp +=25
                 hero.ac-= 20
                 hero.inventory.update({"Leather Hide"
                       })
                 print("Health increased to: {}".format(hero.hp))
                 print("you have ",hero.ac,"gold left")
                 print("your inventory is ",hero.inventory,)

            elif armselection == 2:
                 if hero.ac<34:
                  print("You dont have enoyugh gold!")
                 
                 else:
                  leather_hide = Item('Leather Hide', 5, 0)
                  IsLeatherHideEquipped = True
                  hero.hp +=25
                  hero.ac-= 20
                  hero.inventory.update({"warmogs Armor"
                       })
                  print("Health increased to: {}".format(hero.hp))
                  print("you have ",hero.ac,"gold left")
                  print("your inventory is ",hero.inventory,)
                 
    elif selection == 3:
            if  hero.ac >0:
              print (" you are now in the spellbook Shop")
              print ("1.Magic Robe 40$\n2.Ancient Void staff (26)")
              arm = int(input("enter a value: "))    



            if arm==1:

                if hero.ac<40:
                 print("You dont have enoyugh gold!")
              
                else:
                 leather_hide = Item('Leather Hide', 5, 0)
                 IsLeatherHideEquipped = True
                 hero.hp +=75
                 hero.ac-= 20
                 hero.inventory.update({"Magic Robe"
                       })
                 print("Health increased to: {}".format(hero.hp))
                 print("you have ",hero.ac,"gold left")
                 print("your inventory is ",hero.inventory,)

            elif arm==2:

                 
                if hero.ac<40:
                 print("You dont have enoyugh gold!")
              
                else:
                 leather_hide = Item('Leather Hide', 5, 0)
                 IsLeatherHideEquipped = True
                 hero.damage +=75
                 hero.ac-= 26
                 hero.inventory.update({"Ancient Void Staff"
                       })
                 print("Your spell power is  increased to: {}".format(hero.damage))
                 print("=================")
                 print("")
                 print("you have ",hero.ac,"gold left")
                 print("your inventory is ",hero.inventory,)
                 arm = int(input("press 1 to exit the shop "))   


    elif selection == 4:
           print("you have now exited the shop")
