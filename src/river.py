class River:
    def __init__(self, name):
        self.name = name
        self.contents = []

    def lose_fish(self, fish):
        self.contents.remove(fish)
