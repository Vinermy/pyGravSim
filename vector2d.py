from math import *


class Vector2D(object):
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def normalize(self):
        self.x = self.x / self.length()
        self.y = self.y / self.length()

    def stretch(self, newlength: float):
        factor = newlength / self.length()
        self.x *= factor
        self.y *= factor

    def length(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __mul__(self, factor: float):
        return Vector2D(self.x * factor, self.y * factor)

    def getxy(self):
        return self.x, self.y
