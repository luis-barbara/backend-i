from typing import Protocol


class Animal:
    def __init__(self, name, hp, xp):
        self.name = name
        self.hp = hp
        self.xp = xp

class Runnable(Protocol):
    def run(self):
        pass
    

class Dog(Animal, Runnable):
    def __init__(self, name, hp, xp):
        super().__init__(name, hp, xp)

    def run(self):
        self.run_stat = 30
        print("")

Bob = Dog("Bob",100,10)

Bob.run()


animals:list[Runnable] = [Animal(), Dog(), Animal]

for animal in animals:
    animal.run()