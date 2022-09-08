import sys
from FK import Game

from items.items import create_armor, create_weapon, set_armor, set_weapon

from avatar.avatar import create_avatar, set_avatar


def print_parts(parts):
    print(parts)
    for i in range(len(parts)):
        print(f"{i}:", f"{parts[i]}")


def main(game):
    list_key = game.menu_items
    print_parts(list_key)
    option = int(input("Choose option: "))
    getattr(game, game.menu_items[option])()


if __name__ == '__main__':
    game = Game()
    while True:
        main(game)
