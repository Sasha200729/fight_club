import json

from settings import BASE_DIR
from utils import save_data
avatars_path = BASE_DIR.joinpath("avatar/save_folder/avatars.json")


class Avatar:

    body_parts = ["head", "torso", "leg", "hand"]
    attack = 0
    defence = 0

    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def __str__(self):
        return "Name:{0}, Hp:{1}, Power:{2}".format(
            self.name,
            self.hp,
            self.power
        )


    def __truediv__(self, other):
        # Как проходит операция деления.
        if self.attack != other.defence:
            other.hp = other.hp - self.power
        if self.defence != other.attack:
            self.hp = self.hp - other.power
        return self


    def get_data_for_save(self):
        return {
            "name": self.name,
            "hp": self.hp,
            "power": self.power
            }

    def set_amunition(self, item, name_item, avatar_parameter):
        if getattr(self, name_item, None):
            setattr(
                self,
                avatar_parameter,
                getattr(self, avatar_parameter)
                - getattr(item, avatar_parameter)
            )
        setattr(self, name_item, item)
        setattr(
            self,
            avatar_parameter,
            getattr(self, avatar_parameter) + getattr(item, avatar_parameter)
        )

    def set_armor(self, armor):
        if self.armor:
            self.hp -= self.armor.hp
        self.armor = armor
        self.hp += self.armor.hp

    def set_weapon(weapon):
        if self.weapon:
            self.power -= self.weapon.power
        self.weapon = weapon
        self.power += self.weapon.power

with open(avatars_path) as f:
    avatars_list = [Avatar(**i) for i in json.load(f)]


def print_parts(parts):

    for i in range(len(parts)):
        print(f"{i}:", f"{parts[i]}")


def create_avatar():
    global avatars_list
    name = input("Name:")
    hp = int(input("HP:"))
    power = int(input("Power:"))
    avatars_list += [Avatar(name, hp, power)]
    save_data(avatars_path, [i.get_data_for_save() for i in avatars_list])


def set_avatar():
    global avatars_list
    print_parts(avatars_list)
    avatar = avatars_list[int(input("Choose: "))]
    print(avatar)
