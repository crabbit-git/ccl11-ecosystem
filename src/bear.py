class Bear:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.stomach = []

    def roar(self):
        return "Miaow"
    
    def chow_down(self, fish):
        self.stomach.append(fish)
    
    def gut_inspector(self):
        return len(self.stomach)
