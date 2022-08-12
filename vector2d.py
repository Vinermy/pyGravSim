from math import sqr, sqrt

class vector2d(object):
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)
        self.length = float(sqrt(sqr(self.x) + sqr(self.y)))

    def __add__(self, other):
        return vector2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return vector2d(self.x - other.x, self.y + other.y)

    def normalize(self):
        self.x = self.x / self.length
        self.y = self.y / self.length
        self.length = 1

    def stretch(self, newLength: float): #Set verctor2d's x & y components so that it's length is equal to newLength parameter
        factor = newLength / self.length
        self.x *= factor
        self.y *= factor
        self.length = newLength