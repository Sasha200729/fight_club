import sys
from FK import start ,  Game

from items.items import create_armor, create_weapon, set_armor, set_weapon

from avatar.avatar import  create_avatar, set_avatar


def exit():
    sys.exit("EXIT")



MENU_ITEMS = {
    "start": start,
    "Create armor": create_armor,
    "Create weapon": create_weapon,
    "Set armor": set_armor,
    "Set weapon": set_weapon,
    "Create avatar": create_avatar,
    "Set avatar" : set_avatar,
    "exit": exit
}


def print_parts(parts):
    print(parts)
    for i in range(len(parts)):
        print(f"{i}:", f"{parts[i]}")


def main():
    game = Game()
    list_key = game.menu_items
    print_parts(list_key)
    option = int(input("Choose option: "))
    getattr(game, game.menu_items[option])()


if __name__ == '__main__':
    while True : main()
