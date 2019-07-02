import math

class Vector:
	
    def __init__(self,X,Y,Z):
        self.X = X
        self.Y = Y
        self.Z = Z

    def length(self):
        return math.sqrt(self.X*self.X + self.Y*self.Y + self.Z*self.Z)      

    def multiplyScalar(self,t):
        return Vector(self.X*t, self.Y*t,self.Z*t)

    def add(self,o):
        return Vector(self.X+o.X, self.Y+o.Y,self.Z+o.Z)