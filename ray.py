from vector import Vector
import math


class Ray:
    
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction
  

    def pointAtParameter(self,t):
        return self.a + self.b*multiplyScalar(t)
    

    def hit_sphere(self,center,radius,r):
        oc = r.origin.subtract(center)
        a = r.direction.dot(r.direction)
        b = oc.multiplyScalar(2.0).dot(r.direction)
        c = oc.dot(oc).subtractScalar(radius*radius)
        discriminant = b.multiply(b).subtract(a.multiply(c).multiplyScalar(-4))
        
        return (discriminant.X + discriminant.Y + discriminant.Z ) > 0
   

    def color(self):
        r = self.hit_sphere(Vector(0.0, 0.0, -1.0), 0.5, self)

        if r:
            return Vector(1.0, 0.0, 0.0)

        unitDirection = self.direction.normalize()
        t = 0.5 * (unitDirection.Y + 1.0)
        white = Vector(1.0, 1.0, 1.0)
        blue = Vector(0.5, 0.7, 1.0)

        return white.multiplyScalar(1.0 - t).add(blue.multiplyScalar(t))