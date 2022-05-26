class Phone:

    def __init__(self, n, p, s, m, c):
        # property of instance
        self.model_number = n
        self.proccesor = p
        self.screen = s
        self.memory = m
        self.camera = c

    def __str__(self):
        # call the name of model if we convert object to string
        return self.model_number

    def print_characteristic(self):
        print(
            f"Model:{self.model_number}",
            f"Proccesor:{self.proccesor}",
            f"Memory:{self.memory}",
            sep="\n"
        )

    def call(self):
        # Abstract/polymorfism
        print("Please change me")


class ApplePhone(Phone):

    def __init__(self, name, *args):
        super().__init__(*args)
        self.name = name

    def call(self):
        print("How are you! Hello")


class SamsungPhone(Phone):

    def call(self):
        print("Hello! How are you!")


apple_phone = ApplePhone("My phone", "IPhone 5",
                         "intel", "500X600", 4, "Zeins")
samsung_phone = SamsungPhone("Samsung x7", "raizer", "600x600", 5, "Meinze")
apple_phone.call()
samsung_phone.call()
print(f'{apple_phone.name}:', apple_phone.screen)
print(f'{samsung_phone.name}:', samsung_phone.screen)
