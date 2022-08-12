from celestialBody import celestialBody
from vector2d import vector2d
from math import sqr
import configparser as cp

config = cp.ConfigParser()
config.read("config.ini")

G = float(config["CONSTANTS"]["G"])*(10**-11)

def calculate_forces(body: celestialBody, other: list):
    for other_body in other:
        assert type(other_body) == celestialBody, "All objects in the list must be exemplars of 'celestialBody' class"
        direction = other_body.position - body.position
        force = G * ((body.mass * other_body.mass) / sqr(direction.length))
        direction = direction.normalize()
        acceleration = force / body.mass
        