
import os

import random

go = True
IsShopLocked = False
IsDaggerEquipped = False
IsSpellBookEquipped=False
IsSwordEquipped = False
IsLeatherHideEquipped = False

IsQuest=False




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

class AI(object):
#Represents the enemy player in the game
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

class Item(object):
#represents any item in the game
    def __init__(self, name, hvalue, strvalue):
        self.name = name
        self.hvalue = hvalue
        self.strvalue = strvalue
class Orc:
    def __init__(self):
       self.name = 'a goblin'
       self.damage=15
       self.health=100
                      
os.system("color 06")
os.system("cls")
os.system('color 2f')




def first_boss():
    return CombatEntity(
        display_name="Even larger bear",
        attacks=[
            attack.Attack(
                name="slash",
                display_name="Slash",
                type_=attack.MELEE,
                damage=3,
                description_of_being_used="slashe",
                stamina_cost=3
            ),
            attack.Attack(
                name="bite",
                display_name="Bite",
                type_=attack.MELEE,
                damage=6,
                description_of_being_used="bite",
                stamina_cost=4
            )
        ],
        maximum_health=25,
        maximum_stamina=20,
        strength=10,
        defence=15,
        dexterity=6,
        composure=7,
        critical_hit_chance=4
    )

def second_boss():
    return CombatEntity(
        display_name="The poor, out-of-place lion",
        attacks=[
            attack.Attack(
                name="slash",
                display_name="Slash",
                type_=attack.MELEE,
                damage=8,
                description_of_being_used="slashe",
                stamina_cost=6
            ),
            attack.Attack(
                name="bite",
                display_name="Bite",
                type_=attack.MELEE,
                damage=14,
                description_of_being_used="bite",
                stamina_cost=8
            )
        ],
        maximum_health=40,
        maximum_stamina=50,
        strength=15,
        defence=25,
        dexterity=7,
        composure=8,
        critical_hit_chance=4
    )
