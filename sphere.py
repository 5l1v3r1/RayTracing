import math

from hitRecord import HitRecord
from hitable import Hitable
from vector import Vector

class Sphere(Hitable):
    def __init__(self, center, radius):
        """
        type center: Vector
        type radius: float
        """
        self.center = center
        self.radius = radius

    def hit(self, r, tMin, tMax):
        oc = r.origin - self.center
        a = r.direction.dot(r.direction)
        b = 2 * r.direction.dot(oc)
        c = oc.dot(oc) - (self.radius*self.radius)

        discriminant = b*b - 4*a*c

        if discriminant > 0.0:
            rec = HitRecord()
            temp = (-b - math.sqrt(discriminant)) / (2*a)
            if tMin < temp < tMax:
                rec.t = temp
                rec.p = r.pointAtParameter(rec.t)
                rec.normal = (rec.p - self.center).divideScalar(self.radius)
                return rec

            temp = (-b + math.sqrt(discriminant)) / (2*a)
            if tMin < temp < tMax:
                rec.t = temp
                rec.p = r.pointAtParameter(rec.t)
                rec.normal = (rec.p - self.center).divideScalar(self.radius)
                return rec

        return None