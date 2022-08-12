from celestialBody import celestialBody
from vector2d import vector2d
from math import sqr
import configparser as cp

config = cp.ConfigParser()
config.read("config.ini")

G = float(config["CONSTANTS"]["G"])*(10**-11) #Gravitational constant

def calculate_forces(body: celestialBody, other: list):
    body.affected_by = []
    for other_body in other:
        if other_body.position == body.position: #Do not calculate force from itself
            continue
        assert type(other_body) == celestialBody, "All objects in the list must be exemplars of 'celestialBody' class"
        direction = other_body.position - body.position                      #Vector connecting centers of affecting and affected body
        force = G * ((body.mass * other_body.mass) / sqr(direction.length))  #Numeric value of gravitational force
        acceleration = force / body.mass
        direction.stretch(acceleration)                                      #direction now represents the acceleration
        body.affected_by.append((direction.x, direction.y))
    
def apply_forces(body: celestialBody):
    summ = vector2d(0, 0)          #Resulting acceleration's vector representation
    for force in body.affected_by: #Summ all the accelerations that body is affected by
        summ += force              
    body.speed += summ             #Add the resulting acceleration to current speed
    body.position += body.speed    #Move the body accordinly

def calculate_step(bodies: list): #Update the simulation
    for body in bodies:
        calculate_forces(body=body, other=bodies)
    for body in bodies:
        apply_forces(body=body)
    