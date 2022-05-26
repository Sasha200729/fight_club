class TV:
    """docstring for TV."""

    def __init__(self, quality, size, display, control):
        self.quality = quality
        self.size = size
        self.display = display
        self.control = control

    def watch(self):
        print("Disovery")


class Xiaomy(TV):
    pass


class Samsung(TV):

    def watch(self):
        print("Inter")
