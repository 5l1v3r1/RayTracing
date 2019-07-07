import math


class Vector:
    
    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        self.x = x
        self.y = y
        self.z = z


    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)      

    def multiplyScalar(self,t):
        return Vector(self.x * t, self.y * t, self.z * t)

    def __mul__(self,t):
        return Vector(self.x * t.x, self.y * t.y, self.z * t.z)

    def __add__(self,o):
        return __class__(self.x + o.x, self.y + o.y,self.z + o.z)

    def subtractScalar(self,t):
        return Vector(self.x - t, self.y - t, self.z - t)

    def __sub__(self,o):
        return __class__(self.x - o.x, self.y - o.y, self.z - o.z)
    
    def dot(self,o):
        return self.x * o.x + self.y * o.y + self.z * o.z

    def normalize(self):
        l = self.length()
        return Vector(self.x / l, self.y / l, self.z / l)