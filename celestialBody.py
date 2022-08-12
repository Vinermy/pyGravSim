from vector2d import vector2d

class celestialBody(object): #Class that deals with all the bodies on the screen
    def __init__ (self, position: vector2d, speed: vector2d, mass: float, radius: float):
        self.position = position
        self.speed = speed
        self.mass = mass                                                                       
        self.radius = radius  #Only for drawing on the screen, does not affect simulation
        self.affected_by = [] #List of vector2d. All forces that this body is affected by
