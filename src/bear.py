class Bear:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.stomach = []

    def roar(self):
        return "Miaow"
    
    def chow_down(self, fish):
        self.stomach.append(fish)
    
    def food_count(self):
        return len(self.stomach)
