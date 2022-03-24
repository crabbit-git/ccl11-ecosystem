class River:
    def __init__(self, name):
        self.name = name
        self.contents = []
    
    def population_check(self):
        return len(self.contents)

    def lose_fish(self, fish):
        fish_ID = self.contents.index(fish)
        self.contents.pop(fish_ID)
        # You could also just do self.contents.remove(fish), which works fine,
        # but using pop means the function returns the fish at the end,
        # which you can divert into the bear's fish-eating function in one line.
