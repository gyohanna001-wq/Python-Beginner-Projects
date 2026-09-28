class Mosquito:
    def __init__(self):
        print("Mosquito is created.")

    def whoAmI(self):
        print("I am a mosquito.")

    def fly(self):
        print("Mosquitoes can fly.")

    def swim(self):
        print("Mosquitoes can't swim.")


class Pupae(Mosquito):
    def __init__(self):
        #super.__init__()
        print("Pupae is created.")

    def whoAmI(self):
        print("I am a mosquito pupae.")

    def fly(self):
        print("Mosquito pupae can't fly.")

    def swim(self):
        print("Mosquito pupae can swim.")


class Larvae(Mosquito):
    def __init__(self):
        #super.__init__()
        print("Larvae is created.")

    def whoAmI(self):
        print("I am mosquito larvae.")

    def fly(self):
        print("Mosquito larvae can't fly.")

    def swim(self):
        print("Mosquito larvae can swim.")


# Where polymorphism starts.
def can_it_fly(a):
    a.fly()

mosquito = Mosquito()
pupae = Pupae()
larvae = Larvae()

print("# ------------------- Fly Test ------------------- #")
can_it_fly(mosquito)
can_it_fly(pupae)
can_it_fly(larvae)

