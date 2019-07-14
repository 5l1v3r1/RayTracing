from random import random
import math
import sys

from hitRecord import HitRecord
from vector import Vector

class Ray:
    
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction
  

    def pointAtParameter(self,t):
        return self.origin + self.direction.multiplyScalar(t)

       
    def hit_sphere(self,center,radius,r):
        '''
        determining if a point is on a sphere is as follows:
        dot((p - C),(p - C)) = R * R
        Where p is the point, C is the center of our sphere, and R is the sphere radius.
        '''

        '''
        ray => p(t) = A + t * B
        A is the ray origin, B is the ray direction, and t is a real number.
        So,
        dot((p - C),(p - C)) = R * R <==> dot((p(t) - C),(p(t) - C)) = R * R
        Which expands to:
        dot((A + t * B - C),(A + t * B - C)) = R * R
        Expanding and moving all terms to the LHS, we get:
        t * t * dot(B, B) + 2 * t * dot(A-C, A-C) + dot(C, C)
        The equation above is quadratic.We can use the quadratic formula to solve for t. 
        When solving the quadratic,
        there is the discriminant portion of the equation (b * b - 4ac).
        Which tells us the number of solutions.
        '''    
        
        # A - C
        oc = r.origin - center
        # dot(B, B)
        a = r.direction.dot(r.direction)
        # 2 * dot(A-C, A-C)
        b = 2 * r.direction.dot(oc)
        c = oc.dot(oc) - (radius*radius)
        discriminant = b*b - 4*a*c

        if (discriminant < 0):
            return -1.0; 
        else:
            return (-b - math.sqrt(discriminant)) / (2*a)     
    

    def randomInUnitSphere(self):
        while True:
            p = Vector(random(), random(), random())
            p = p.multiplyScalar(2.0) - Vector(1.0, 1.0, 1.0)
            if p.dot(p) < 1.0:
                return p


    def color(self,world):
        hitInfo = world.hit(self, 0, sys.float_info.max)

        if hitInfo is not None:
            target = hitInfo.p + hitInfo.normal + self.randomInUnitSphere()
            r = Ray(hitInfo.p, target - hitInfo.p)
            return r.color(world).multiplyScalar(0.5)

        unitDirection = self.direction.normalize()
        t = 0.5 * (unitDirection.y + 1.0)
        white = Vector(1.0, 1.0, 1.0)
        blue = Vector(0.5, 0.7, 1.0)

        return white.multiplyScalar(1.0 - t) + blue.multiplyScalar(t)