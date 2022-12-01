#from tkinter import *
from tkinter import Tk, Label, Button, Entry, Toplevel, Frame
import json
import sys
from utils import save_data
from random import randint
from items.items import Armor, Weapon, armors_path, weapons_path
from avatar.avatar import Avatar, avatars_path, enemies_path


def print_parts(parts):
    for i in range(len(parts)):
        print(f"{i}:", f"{parts[i]}")


class GameWindow:
    window = Tk()

    def __init__(self):
        self.window.title("Main menu")
        self.window.geometry('400x250')
        self.btn = Button(
            self.window,
            text="Create armor",
            command=self.create_armor
        )
        self.btn2 = Button(
            self.window,
            text="Create weapon",
            command=self.create_weapon
        )
        self.btn3 = Button(
            self.window,
            text="Create avatar",
            command=self.create_avatar
        )
        self.btn4 = Button(
            self.window,
            text="Create enemy",
            command=self.create_enemy
        )
        # self.btn.grid(column=2, row=0)
        # self.btn2.grid(column=2, row=1)
        # self.btn3.grid(column=2, row=2)
        # self.btn4.grid(column=2, row=3)
        self.btn_exit = Button(self.window, text="Exit",
                               command=self.window.destroy)
        #self.btn_exit.grid(column=0, row=1)
        self.btn.pack()
        self.btn2.pack()
        self.btn3.pack()
        self.btn4.pack()
        self.btn_exit.pack()

    def clicked(self):
        self.lbl.configure(text=self.txt.get())
        # print(*dir(self.txt),sep = "\n")
        print(self.txt.get())

    def open_window(self):
        self.window.mainloop()

    def create_weapon(self):
        tk = Tk()
        newWindow = Frame(tk)
        tk.title("Create weapon")
        tk.geometry('400x250')
        labelExample = Label(newWindow, text="Create weapon")
        labelExample.grid(column=3, row = 5)
        entry = Entry(newWindow, width = 10)
        eentry = Entry(newWindow, width = 10)
        enstry = Entry(newWindow, width = 10)
        qentry = Entry(newWindow, width = 10)

        buttonExample = Button(newWindow, text="Create weapon")

        btn_exit = Button(
            newWindow,
            text="Exit",
            command=tk.destroy
        )
        newWindow.pack()
        labelExample.pack()
        buttonExample.pack()
        entry.pack()
        eentry.pack()
        enstry.pack()
        qentry.pack()


        btn_exit.pack()

        tk.mainloop()

    def create_armor(self):
        tk = Tk()
        newWindow = Frame(tk)
        tk.title("Create armor")
        tk.geometry('400x250')
        labelExample = Label(tk, text="Create armor")
        buttonExample = Button(tk, text="Create armor")
        entry = Entry(tk, width = 10)
        eentry = Entry(tk, width = 10)
        enstry = Entry(tk, width = 10)
        qentry = Entry(tk, width = 10)
        labelExample.pack()
        entry.pack()
        eentry.pack()
        enstry.pack()
        qentry.pack()
        buttonExample.pack()
        tk.mainloop()


    def create_avatar(self):
        tk = Tk()
        newWindow = Frame(tk)
        tk.title("Create avatar")
        tk.geometry('400x250')
        labelExample1 = Label(tk, text="Create avatar")
        buttonExample2 = Button(tk, text="Create avatar")
        buttonExample1 = Button(tk, text="Set avatar")
        entry = Entry(tk, width = 7)
        eentry = Entry(tk, width = 10)
        enstry = Entry(tk, width = 10)
        qentry = Entry(tk, width = 10)
        labelExample1.pack()
        buttonExample2.pack()
        buttonExample1.pack()
        entry.pack()
        eentry.pack()
        enstry.pack()
        qentry.pack()
        tk.mainloop()

    def create_enemy(self):
        tk = Tk()
        newWindow = Frame(tk)
        tk.title("Create enemy")
        tk.geometry('400x250')
        labelExample = Label(tk, text="Create enemy")
        buttonExample = Button(tk, text="Create enemy")
        entry = Entry(tk, width = 10)
        eentry = Entry(tk, width = 10)
        enstry = Entry(tk, width = 10)
        qentry = Entry(tk, width = 10)
        labelExample.pack()
        buttonExample.pack()
        entry.pack()
        eentry.pack()
        enstry.pack()
        qentry.pack()
        tk.mainloop()


class Game:
    avatar = None
    boss = None
    menu_items = [
        'start',
        'set_weapon',
        'create_weapon',
        'set_avatar',
        'create_avatar',
        'set_armor',
        'create_armor',
        'create_enemy',
        'set_enemy',
        'set_enemy_armor',
        'set_enemy_weapon',
        'view',
        'exit'
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
        with open(enemies_path) as f:
            self.enemies = [Avatar(**i) for i in json.load(f)]

    def exit(self):
        sys.exit("EXIT")

    def create_avatar(self):
        name = input("Name:")
        hp = int(input("HP:"))
        power = int(input("Power:"))
        self.avatars += [Avatar(name, hp, power)]
        save_data(avatars_path, [i.get_data_for_save() for i in self.avatars])

    def create_weapon(self):
        name = input("Name:")
        size = int(input("Size:"))
        durability = int(input("Durability:"))
        power = int(input("Power:"))
        self.weapons += [Weapon(name, size, durability, power)]
        save_data(weapons_path, [i.get_data_for_save() for i in self.weapons])

    def set_weapon(self):

        print(self.avatar)
        if self.avatar is None:
            print('Choose avatar before set weapon')
            return False

        print_parts(self.weapons)
        weapon = self.weapons[int(input("Choose: "))]
        self.avatar.set_amunition(weapon, "weapon", "power")
        print(weapon)

    def set_armor(self):
        print(self.avatar)
        if self.avatar is None:
            print('Choose avatar before set armor')
            return False

        print_parts(self.armors)
        armor = self.armors[int(input("Choose: "))]
        self.avatar.set_amunition(armor, "armor", "hp")
        print(armor)

    def set_avatar(self):

        print_parts(self.avatars)
        self.avatar = self.avatars[int(input("Choose: "))]
        print(self.avatar)

    def create_enemy(self):
        name = input("Name:")
        hp = int(input("HP:"))
        power = int(input("Power:"))
        self.enemies += [Avatar(name, hp, power)]
        save_data(enemies_path, [i.get_data_for_save() for i in self.enemies])

    def set_enemy(self):
        print_parts(self.enemies)
        self.boss = self.enemies[int(input("Choose: "))]
        print(self.boss)

    def set_enemy_weapon(self):
        print(self.boss)
        if self.boss is None:
            print('Choose enemies before set weapon')
            return False

        print_parts(self.weapons)
        enemy_weapon = self.weapons[int(input("Choose: "))]
        self.boss.set_amunition(enemy_weapon, "weapon", "power")
        print(enemy_weapon)

    def set_enemy_armor(self):
        print(self.boss)
        if self.boss is None:
            print('Choose enemies before set weapon')
            return False
        print_parts(self.armors)
        enemy_armor = self.armors[int(input("Choose: "))]
        self.boss.set_amunition(enemy_armor, "armor", "hp")
        print(enemy_armor)

    def start(self):
        while self.avatar.hp > 0 and self.boss.hp > 0:

            print("Choose parts for attack")
            print_parts(self.boss.body_parts)
            self.avatar.attack = int(input("part number: "))
            print("Choose parts for defence")
            print_parts(self.avatar.body_parts)
            self.avatar.defence = int(input("part number: "))
            # here
            attack_part = randint(0, len(self.avatar.body_parts)-1)
            self.avatar.attack = attack_part
            print("Enemy attack:", self.avatar.body_parts[attack_part])
            defence_part = randint(0, len(self.boss.body_parts)-1)
            self.boss.defence = defence_part
            print("Enemy defence:", self.avatar.body_parts[defence_part])
            self.avatar / self.boss
            print("avatar: ", self.avatar.hp)
            print("boss: ", self.avatar.hp)

    def __str__(self):

        return '\n'.join([str(self.avatar), str(self.boss)])

    def view(self):
        print(self)
        input()

#game -= Game()
# print(game.enemies)
