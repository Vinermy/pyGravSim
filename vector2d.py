from math import *


class Vector2D(object):
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)
        self.length = float(sqrt((self.x ** 2 + self.y ** 2)))

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def normalize(self):
        self.x = self.x / self.length
        self.y = self.y / self.length
        self.length = 1

    # Set verctor2d's x & y components so that it's length is equal to newLength parameter
    def stretch(self, newLength: float):
        factor = newLength / self.length
        self.x *= factor
        self.y *= factor
        self.length = newLength

    def updateLen(self):
        self.length = float(sqrt(self.x ** 2 + self.y ** 2))
