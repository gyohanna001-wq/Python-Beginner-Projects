class Animal:
    def swim(self):
        print('Swim')

class Lion(Animal):
    def swim(self):
        raise Exception("Lions can't swim!")

def make_animal_swim(animal):
    animal.swim()


animal = Animal()
animal.make_animal_swim()