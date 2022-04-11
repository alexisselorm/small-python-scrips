from collections import namedtuple
from abc import ABC, abstractmethod


class Point:

    default_colour = "yellow"

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def __str__(self):

        return f"({self.x},{self.y})"

    @classmethod
    def zero(cls):

        return cls(0, 0)

    def __eq__(self, o):

        return self.x == o.x and self.y == o.y

    def __gt__(self, o):

        return self.x > o.x and self.y > o.y

    def __add__(self, o):

        return Point(self.x+o.x, self.y+o.y)

    def draw(self):

        print(f" Point ({self.x},{self.y})")


Point.default_colour = "red"

point = Point.zero()
print(point)

print(Point.default_colour)

who = Point(5, 6)

who.draw()


print(who)


# Comparing objects

point = Point(10, 20)

other = Point(1, 2)

print(point == other)

print(point > other)

print(point < other)


# Arithmetic ops

print(point + other)


# Making custom containers

class TagCloud:

    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        len(self.__tags)

    def __iter__(self, tag):
        return iter(self.__tags)


cloud = TagCloud()

cloud.add("python")

cloud.add("python")

cloud.add("python")

cloud.add("python")

cloud["python"] = 10
# Still accesses tags
print(cloud._TagCloud__tags)
# throws an error that object has no attribute called tags. reason : __(double underline)
# print(cloud.__tags)


class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


product = Product(10)
print(product.price)
product.price = 20
print(product.price)


# Inheritance
# mammal and fish inherits the eat from the animal class
class Animal:
    def __init__(self):
        print("Animal constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal constructor")
        self.weight = 3

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()
print(m.age)
print(m.weight)
print(isinstance(m, Animal))

# A good example of inheritance


class InvalidOperationError:
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("reading data from a network")


class MemoryStream(Stream):
    def read(self):
        print("reading data from memory")


# Polymorphism
class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    print("TextBox")


class DropDownList(UIControl):
    print("list")


def draw(controls):
    for control in controls:
        control.draw()


Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)
