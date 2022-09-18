from typing import Iterable
from celestialBody import CelestialBody
from vector2d import Vector2D
import configparser as cp

config = cp.ConfigParser()
config.read("config.ini")

G = float(config["CONSTANTS"]["G"])*(10**-11) #Gravitational constant
print(G)

def calculate_forces(body: CelestialBody, others: Iterable[CelestialBody]):
    body.affected_by = []
    for other_body in others:
        try:
            force = G * (other_body.mass / (other_body.position - body.position).length ** 2)
            vector = other_body.position - body.position
            vector.stretch(force)
            body.affected_by.append(vector)
        except ZeroDivisionError:
            continue
    
def apply_forces(body: CelestialBody):
    for force in body.affected_by: #Summ all the accelerations that body is affected by
        body.speed += force              
    body.position += body.speed    #Move the body accordinly

def calculate_step(bodies: Iterable[CelestialBody]): #Update the simulation
    for body in bodies:
        calculate_forces(body=body, others=bodies)
    for body in bodies:
        apply_forces(body=body)
    