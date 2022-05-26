from FK import start
from items.items import create_armor, create_weapon


def set_armor():
    pass


def set_weapon():
    pass


MENU_ITEMS = {
    "start": start,
    "Create armor": create_armor,
    "Create weapon": create_weapon,
    "Set armor": set_armor,
    "Set weapon": set_weapon
}


def print_parts(parts):
    print(parts)
    for i in range(len(parts)):
        print(f"{i}:", f"{parts[i]}")


def main():
    list_key = list(MENU_ITEMS.keys())
    print_parts(list_key)
    option = int(input("Choose option: "))
    MENU_ITEMS[list_key[option]]()


if __name__ == '__main__':
    main()
