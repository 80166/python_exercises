class Animal(object):
    def speak(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Woof!"


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Meow!"


class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None

    def greet(self):
        return f"Hello, my name is {self.name}."

    def introduce_pet(self):
        if self.pet:
            return f"This is my pet {self.pet.name}."
        else:
            return "I don't have a pet."


class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

    def greet(self):
        return f"Hello, my name is {self.name} and I earn {self.salary} per year."


class Fish(object):
    def swim(self):
        return "Fish swims."


class Salmon(Fish):
    def __init__(self, name):
        self.name = name

    def jump(self):
        return "Salmon jumps upstream."


class Halibut(Fish):
    def __init__(self, name):
        self.name = name

    def camouflage(self):
        return "Halibut changes color to blend with the surroundings."


rover = Dog("Rover")
print(rover.speak())

satan = Cat("Satan")
print(satan.speak())

mary = Person("Mary")
print(mary.greet())
print(mary.introduce_pet())

mary.pet = satan
print(mary.introduce_pet())

frank = Employee("Frank", 120000)
print(frank.greet())
frank.pet = rover
print(frank.introduce_pet())

flipper = Fish()
print(flipper.swim())
