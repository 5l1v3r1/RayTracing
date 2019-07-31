from ray import Ray
from vector import Vector


class Camera:
    def __init__(self):
        self.lowerLeftCorner = Vector(-2.0, -1.0, -1.0)
        self.horizontal = Vector(4.0, 0.0, 0.0)
        self.vertical = Vector(0.0, 2.0, 0.0)
        self.origin = Vector(0.0, 0.0, 0.0)

    def getRay(self, u, v):
        direction = self.lowerLeftCorner + self.horizontal.multiply_scalar(u)
        direction = direction + self.vertical.multiply_scalar(v) - self.origin
        return Ray(self.origin, direction)
