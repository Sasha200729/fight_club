import json

from random import randint
from items.items import Armor, Weapon, armors_path, weapons_path
from avatar.avatar import Avatar, avatars_path


def print_parts(parts):
    for i in range(len(parts)):
        print(f"{i}:", f"{parts[i]}")


def start():
    player = Avatar("Peter", 100, 10)
    enemy = Avatar("Enemy", 200, 5)
    armor = Armor("Dragon armor", 2, 30, 50)
    weapon = Weapon("Dragon sword", 2, 30, 50)
    player.set_amunition(armor, "armor", "hp")
    player.set_amunition(weapon, "weapon", "power")
    print(player.armor, player.hp)
    print(player.weapon, player.power)
    while player.hp > 0 and enemy.hp > 0:

        print("Choose parts for attack")
        print_parts(enemy.body_parts)
        player.attack = int(input("part number: "))
        print("Choose parts for defence")
        print_parts(player.body_parts)
        player.defence = int(input("part number: "))
        # here
        attack_part = randint(0, len(player.body_parts)-1)
        enemy.attack = attack_part
        print("Enemy attack:", player.body_parts[attack_part])
        defence_part = randint(0, len(enemy.body_parts)-1)
        enemy.defence = defence_part
        print("Enemy defence:", player.body_parts[defence_part])
        player / enemy
        print("player: ", player.hp)
        print("enemy: ", enemy.hp)






class Game:
    avatar = None
    boss = None
    menu_items = [
        'set_weapon' ,
        'create_weapon' ,
        'set_avatar' ,
        'create_avatar' ,
        'set_armor' ,
        'create_armor' ,
        ]

    def __init__(self):
        self.enemies = []
        self.items = []

        self.skills = []

        with open(avatars_path) as f:
            self.avatars = [Avatar(**i) for i in json.load(f)]
        with open(armors_path) as f:
            self.armors = [Armor(**i) for i in json.load(f)]
        with open(weapons_path) as f:
            self.weapons = [Weapon(**i) for i in json.load(f)]

    def create_avatar(self):
        name = input("Name:")
        hp = int(input("HP:"))
        power = int(input("Power:"))
        self.avatars += [Avatar(name, hp, power)]
        save_data(avatars_path, [i.get_data_for_save() for i in self.avatars])

    def set_avatar(self):
        print_parts(self.avatars)
        avatar = self.avatars[int(input("Choose: "))]
        print(avatar)

    def create_weapon(self):
        name = input("Name:")
        size = int(input("Size:"))
        durability = int(input("Durability:"))
        power = int(input("Power:"))
        self.weapons += [Weapon(name, size, durability, power)]
        save_data(weapons_path, [i.get_data_for_save() for i in self.weapons])

    def set_weapon(self):

        print_parts(self.weapons)
        weapon = self.weapons[int(input("Choose: "))]
        print(weapon)


    def set_armor(self):

        print_parts(self.armors)
        armor = self.armors[int(input("Choose: "))]
        print(armor)


    def set_avatar(self):

        print_parts(self.avatars)
        avatar = self.avatars[int(input("Choose: "))]
        print(avatar)












#game -= Game()
#print(game.enemies)
