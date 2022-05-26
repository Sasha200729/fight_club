class Avatar:

    body_parts = ["head", "torso", "leg", "hand"]
    attack = 0
    defence = 0

    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def __truediv__(self, other):
        # Как проходит операция деления.
        if self.attack != other.defence:
            other.hp = other.hp - self.power
        if self.defence != other.attack:
            self.hp = self.hp - other.power
        return self

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
