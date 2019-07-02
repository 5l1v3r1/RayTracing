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

    def multiply(self,t):
        return Vector(self.X*t.X, self.Y*t.Y,self.Z*t.Z)

    def add(self,o):
        return Vector(self.X+o.X, self.Y+o.Y,self.Z+o.Z)

    def subtractScalar(self,t):
        return Vector(self.X - t, self.Y - t, self.Z - t)

    def subtract(self,o):
        return Vector(self.X - o.X, self.Y - o.Y, self.Z - o.Z)
    
    def dot(self,o):
        return Vector(self.X * o.X, self.Y * o.Y, self.Z * o.Z)

    def normalize(self):
        l = self.length()
        return Vector(self.X / l, self.Y / l, self.Z / l)