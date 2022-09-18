from vector2d import Vector2D


class CelestialBody:  # Class that deals with all the bodies on the screen
    def __init__(self, position: Vector2D, speed: Vector2D, mass: int, radius: int):
        self.position = position
        self.speed = speed
        self.mass = mass
        self.radius = radius  # Only for drawing on the screen, does not affect simulation
        self.affected_by = []  # List of vector2d. All forces that this body is affected by
