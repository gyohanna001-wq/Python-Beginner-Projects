"""
Polymorphism:
(many forms)
It refers to the same object (or function) exhibiting different forms and behaviors.
"""

# parent class
class Bird:
    def __init__(self):
        print('Bird is created.')

    def whoAmI(self):
        print('I am a Bird.')

    def fly(self):
        print('Birds can fly.')

    def swim(self):
        print('Birds can swim.')


# child class
class Owl(Bird):

    # We write parent class/classes inside parenthesis

    def __init__(self):
        # first -> we call __init__() of Super class (super() == Bird)
        # super().__init__()
        print('Owl is created.')

    # override the parent methods
    def whoAmI(self):
        print('I am an Owl.')

    def fly(self):
        print('Some owls can not fly.')

    def swim(self):
        print('Owls can not swim.')

    # Owls have night vision
    def night_vision(self):
        print('Owls have night vision.')


# penguin class
class Penguin(Bird):
    def __init__(self):
        # super().__init__()
        print('Penguin is created.')

    # override the parent methods
    def whoAmI(self):
        print('I am a Penguin.')

    # override fly
    def fly(self):
        print('Penguins can not fly.')

    # leave the swim method as it is


# two child classes from the same parent class
# Owl, Penguin <---- Bird

# common function
def can_it_fly(bird):
    # call the fly method on the parameter bird
    bird.fly()


# call with three objects -> Bird, Owl, Penguin
bird = Bird()
owl = Owl()
penguin = Penguin()

print("#----------- Fly Test ------------#")
can_it_fly(bird)
can_it_fly(owl)
can_it_fly(penguin)


"""
The same function can_it_fly returns different results based on the object as its parameter.
"""