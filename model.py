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
        if other_body.position == body.position: #Do not calculate force from itself
            continue
        direction = other_body.position - body.position                      #Vector connecting centers of affecting and affected body
        force = G * ((body.mass * other_body.mass) / direction.length ** 2)  #Numeric value of gravitational force
        acceleration = force / body.mass
        direction.stretch(acceleration)                                      #direction now represents the acceleration
        body.affected_by.append((direction.x, direction.y))
    
def apply_forces(body: CelestialBody):
    summ = Vector2D(0, 0)          #Resulting acceleration's vector representation
    for force in body.affected_by: #Summ all the accelerations that body is affected by
        summ += force              
    body.speed += summ             #Add the resulting acceleration to current speed
    body.position += body.speed    #Move the body accordinly

def calculate_step(bodies: list): #Update the simulation
    for body in bodies:
        calculate_forces(body=body, other=bodies)
    for body in bodies:
        apply_forces(body=body)
    