import math


class Vector:
    
    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        self.x = x
        self.y = y
        self.z = z
      
    def __mul__(self,other):
        return __class__(self.x * other.x, self.y * other.y, self.z * other.z)

    def __add__(self,other):
        return __class__(self.x + other.x, self.y + other.y,self.z + other.z)

    def __sub__(self,other):
        return __class__(self.x - other.x, self.y - other.y, self.z - other.z)

    def subtractScalar(self,t):
        return __class__(self.x - t, self.y - t, self.z - t)     

    def multiplyScalar(self,t):
        return __class__(self.x * t, self.y * t, self.z * t)

    def divideScalar(self,t):
        return __class__(self.x / t, self.y / t, self.z / t)

    def normalize(self):
        l = self.length()
        return __class__(self.x / l, self.y / l, self.z / l)

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def dot(self,other):
        return self.x * other.x + self.y * other.y + self.z * other.z