class Animal():
    def __init__(self):
        print("Animal is created.")

    def make_sound():
        print("This is a animal's sound: 'We don't know yet.'")

class Dog(Animal):
    def __init__(self):
        #super.__init__()
        print('Dog is created.')

    def make_sound(self):
        print('Woof!')

class Cat(Animal):
    def __init__(self):
        #super.__init__()
        print('Cat is created.')

    def make_sound(self):
        print('Meow!')

class Cow(Animal):
    def __init__(self):
        #super.__init__()
        print('Cow is created.')

    def make_sound(self):
        print('Moo!')

# Where polymorphism starts
def animal_sound(animal):
    animal.make_sound()


dog = Dog()

cat = Cat()

cow = Cow()

animal_sound(dog)

animal_sound(cat)

animal_sound(cow)




class Shape():
    def __init__(self):
        print("Shape is created.")

    def area():
        print("Area is: 'We don't know yet.'")


class Rectangle(Shape):
    def __init__(self):
        #super.__init__()
        print("Rectangle is created.")


    def area(self):
        length = 10
        width = 2
        print(length * width)


class Circle(Shape):
    def __init__(self):
        #super.__init__()
        print("Circle is created.")

    def area(self):
        radius = 3
        print(3.14 * radius * radius)


class Triangle(Shape):
    def __init__(self):
        #super.__init__()
        print("Triangle is created.")

    def area(self):
        base = 24
        height = 2
        print(0.5 * base * height)


def what_is_the_area(shape):
    shape.area()


rectangle = Rectangle()
circle = Circle()
triangle = Triangle()
what_is_the_area(rectangle)
what_is_the_area(circle)
what_is_the_area(triangle)



class Vehicle():
    def __init__(self):
        print("Vehicle is created.")

    def info():
        print("Wheels: ?")

    def max_speed():
        print("Max Speed: ?")


class Car(Vehicle):
    def __init__(self):
        #super.__init__()
        print("Car is created.")

    def info(self):
        wheels = 4
        print(wheels, "wheels")

    def max_speed(self):
        max_speed = 200
        print("speed:", max_speed, "km/h")


class Bike(Vehicle):
    def __init__(self):
        #super.__init__()
        print("Bike is created.")

    def info(self):
        wheels = 2
        print(wheels, "wheels")

    def max_speed(self):
        max_speed = 120
        print("speed:", max_speed, "km/h")


class Truck(Vehicle):
    def __init__(self):
        #super.__init__()
        print("Truck is created.")

    def info(self):
        wheels = 8
        print(wheels, "wheels")

    def max_speed(self):
        max_speed = 140
        print("speed", max_speed, "km/h")

more_vehicles = ["Ferrari", "Cyber Truck", "Road Bikes", "Mountain Bikes", "Refrigerated Trucks", "Sports Car"]
car = Car()
bike = Bike()
truck = Truck()
more_vehicles[0] = car.info(), car.max_speed()
more_vehicles[1] = truck.info(), truck.max_speed()
more_vehicles[2] = bike.info(), bike.max_speed()
more_vehicles[3] = bike.info(), bike.max_speed()
more_vehicles[4] = truck.info(), truck.max_speed()
more_vehicles[5] = car.info(), car.max_speed()


class Employee():
    def __init__(self):
        print('Employee is created.')

    def calculate_salary():
        print('Salary: ?')

    def get_role():
        print('Role: ?')

class Manager(Employee):
    def __init__(self):
        #super.__init__()
        print('Manager is created.')

    def calculate_salary(self):
        base_salary = 4000
        print(f"Your salary is: {base_salary + 5000}")

    def get_role(self):
        print('Your role is: Manager.')

class Developer(Employee):
    def __init__(self):
        #super.__init__()
        print('Developer is created.')

    def calculate_salary(self):
        base_salary = 3100
        print(f"Your salary is {base_salary + 5000}")

    def get_role(self):
        print('Your role is: Developer.')

class Intern(Employee):
    def __init__(self):
        #super.__init__()
        print('Intern is created.')

    def calculate_salary(self):
        base_salary = 2300
        print(f"Your salary is {base_salary}.")

    def get_role(self):
        print('Your role is: Intern.')

def show_payroll(employees):
    employees.calculate_salary()
    employees.get_role()

manager = Manager()

developer = Developer()

intern = Intern()

show_payroll(manager)
show_payroll(developer)
show_payroll(intern)


class MediaPlayer():
    def __init__(self):
        print('Media Player is created.')

    def play():
        print('Song Playing: ?')

    def pause():
        print('Paused song: ?')

    def stop():
        print('Stopped song: ?')

class MusicPlayer(MediaPlayer):
    def __init__(self):
        #super.__init__()
        print('Music Player is created.')

    def play(self):
        song = "Broken Halos: for KING & COUNTRY"
        print(f'Song playing: {song}')

    def pause(self):
        song = "Broken Halos: for KING & COUNTRY"
        print(f'Paused Song: {song}')

    def stop(self):
        song = "Broken Halos: for KING & COUNTRY"
        print(f'Stopped Song: {song}')

class VideoPlayer(MediaPlayer):
    def __init__(self):
        #super.__init__()
        print('Video Player is created.')

    def play(self):
        print('Video is playing.')

    def pause(self):
        print('Video paused.')

    def stop(self):
        print('Video stopped.')

class PodcastPlayer(MediaPlayer):
    def __init__(self):
        #super.__init__()
        print('Podcast Player is created.')

    def play(self):
        print('Podcast started.')

    def pause(self):
        print('Podcast paused.')

    def stop(self):
        print('Podcast stopped.')

def media_controls(media):
    media.play()
    media.pause()
    media.stop()


music = MusicPlayer()

video = VideoPlayer()

podcast = PodcastPlayer()

media_controls(music)
media_controls(video)
media_controls(podcast)