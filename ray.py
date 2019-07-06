from vector import Vector

class Ray:
    
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction
  
    def pointAtParameter(self,t):
        return self.a + self.b*multiplyScalar(t)

    def color(self):
        unitDirection = self.direction
        t = 0.5 * (unitDirection.Y + 1.0)

        a = Vector(1.0, 1.0, 1.0)
        a = a.multiplyScalar(1.0 - t)

        b = Vector(0.5, 0.7, 1.0)
        b = b.multiplyScalar(t)

        return a.add(b)
