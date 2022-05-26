from random import randint
from items.items import Armor, Weapon
from avatar.avatar import Avatar


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
