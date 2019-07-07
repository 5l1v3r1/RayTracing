from vector import Vector
import math


class Ray:
    
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction
  

    def pointAtParameter(self,t):
        return self.a + self.b*multiplyScalar(t)

       
    def hit_sphere(self,center,radius,r):
        oc = r.origin - center
        a = r.direction.dot(r.direction)
        b = 2 * r.direction.dot(oc)
        c = oc.dot(oc) - (radius*radius)
        discriminant = b*b - 4*a*c

        return discriminant > 0        
    

    def color(self):
        r = self.hit_sphere(Vector(0.0, 0.0, -1.0), 0.5, self)

        if r:
            return Vector(1.0, 0.0, 0.0)

        unitDirection = self.direction.normalize()
        t = 0.5 * (unitDirection.y + 1.0)
        white = Vector(1.0, 1.0, 1.0)
        blue = Vector(0.5, 0.7, 1.0)

        return white.multiplyScalar(1.0 - t) + blue.multiplyScalar(t)