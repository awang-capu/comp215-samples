"""
class ChildClass(ParentClass)
"""

"""
Type A: ChildClass adds no new attributes but only new methods: inherits the constructor of ParentClass
Note: simple, but must check the parent class to know how to construct the object.
"""
# E.g.1:
class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):
        print("Dog barks")


class Cat(Animal):
    def speak(self):
        print("Cat meows")


class Cow(Animal):
    pass


animals = [Dog(), Cat(), Cow()]

for a in animals:
    a.speak()


# E.g.2

# import math

# class Point2D:
#     """A point on the 2D Cartesian plane."""
    
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f'({round(self.x, 2)}, {round(self.y, 2)})'

#     def distance(self, other):
#         """Return the Euclidean distance between this point and another Point2D."""
#         return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


# class LabelledPoint2D(Point2D):
#     """A labelled point on a 2D Cartesian plane."""
#     def __str__(self, label):
#         return f'{label}: ({round(self.x, 2)}, {round(self.y, 2)})'



# p1 = Point2D(1.2345, 2.3456)
# p2 = LabelledPoint2D(3.1415, 4.5678)
# print(p2.__str__('LabelA'))

# print(p1)             # Output: (1.23, 2.35)
# # print(p1.distance(p2)) 
# # print(p2.distance(p1))



"""
Type B: ChildClass adds new attributes: ChildClass defines __init__ and should call super().__init__()
Note: 
Clear explicit initialization. 
Child constructor overrides parent constructor. If still want the parent initialization, call super().__init__()
"""

# E.g. 2.1

import math

class Point2D:
    """A point on the 2D Cartesian plane."""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({round(self.x, 2)}, {round(self.y, 2)})'

    def distance(self, other):
        """Return the Euclidean distance between this point and another Point2D."""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class LabelledPoint2D(Point2D):
    """A labelled point on a 2D Cartesian plane."""
    
    def __init__(self, x, y, label):
        super().__init__(x, y)
        self.label = label

    def __str__(self):
        return f'{self.label}: ({round(self.x, 2)}, {round(self.y, 2)})'


p1 = Point2D(1.2345, 2.3456)
p2 = LabelledPoint2D(3.1415, 4.5678, "A")


print(p1)             # Output: (1.23, 2.35)
print(p2)             # Output: A: (3.14, 4.57)
print(p1.distance(p2)) 
print(p2.distance(p1))



# E.g. 3
# Base class
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print(self.brand, self.model, "is starting.")

    def drive(self):
        print(self.brand, self.model, "is driving.")


# Child class inheriting from Car
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year) # Call the parent class constructor
        self.battery_capacity = battery_capacity

    def charge(self):
        print(self.brand, self.model, "is charging its battery.")

    def start(self): # Override a method from Car
        print(self.brand, self.model, "starts silently with electric power.")


# Child class inheriting from ElectricCar
class Tesla(ElectricCar):
    def __init__(self, model, year, battery_capacity, autopilot_version):
        super().__init__("Tesla", model, year, battery_capacity)
        self.autopilot_version = autopilot_version

    def autopilot(self):
        print(self.model, "is driving using Autopilot version", self.autopilot_version)


# ----- Testing the classes -----

# Create a normal car
car1 = Car("Toyota", "Corolla", 2022)
car1.start()
car1.drive()

print()

# Create an electric car
ecar1 = ElectricCar("Nissan", "Leaf", 2023, "40 kWh")
ecar1.start()
ecar1.drive()
ecar1.charge()

print()

# Create a Tesla
tesla1 = Tesla("Model 3", 2024, "75 kWh", "3.0")
tesla1.start()
tesla1.drive()
tesla1.charge()
tesla1.autopilot()






"""
inheritance and polymorphism

Game: different objects update themselves
Machine learning libraries like scikit-learn use the same methods (fit, predict) for many models
"""
