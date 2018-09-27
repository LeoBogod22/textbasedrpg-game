
class Character:
    def __init__(self,name,hp,damage,ac,inventory,exp,):
        self.name=name
        self.hp=hp
        self.damage=damage
        self.ac=ac
        self.inventory=inventory
        self.exp=exp





class Fighter(Character):
    def __init__(self):
        super().__init__(name=input("What is your characters name?"),damage=20,ac=10,
                         hp=120,inventory={"sword","shield"},exp=10 ,)
    prof = "fighter"
    maxhp=10
    level=1
    hd=10
    level2=20

class warior(Character):
    def __init__(self):
        super().__init__(name=input("What is your characters name?"),damage=20,ac=10,
                         hp=150,inventory={"Dorans Shield", "rusty sword"},exp=8 )
    prof= "cleric"
    maxhp=8
    level=1
    hd=8
    level2=15



class  Mage(Character):
    def __init__(self):
        super().__init__(name=input("What is your characters name?"),damage=20,ac=100,
                         hp=144,inventory={"staff","spellbook"},exp=4)
    prof= "mage"
    mana=1
    maxmana=1
    maxhp=4
    level=1
    hd=4
    level2=10
    ddamage=14
class Goblin:
    def __init__(self):
        super().__init__(name="goblin",
                         hp=150,damage=20,
                         ac=6,inventory={},
                        
                         exp=7)
class Dragon(Character):

  def __init__(self):
        super().__init__(name="grim reaper of death" ,damage=20,ac=10,
                         hp=100,inventory={},exp=4)


drag=Dragon()

class Human(object):
#Represents the human player in the game
    def __init__(self, name, health, strength, gold):
        self.name = name
        self.health = health
        self.strength = strength
        self.gold = gold
