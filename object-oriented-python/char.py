import random

class Character:

class Bard:
    lute = True

    def __init__(self, name, lute=True, **kwargs):
        self.name = name
        self.lute = lute
        for key, value in kwargs.items():
            setattr(self, key, value)

    def play(self):
        return self.lute and bool(random.randint(0, 1))

    def buff(self, target):
        return self.lute and target
