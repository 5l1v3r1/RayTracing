import math
from random import random

from camera import Camera
from hitable_list import HitableList
from ray import Ray
from sphere import Sphere
from vector import Vector

NX = 200
NY = 100
NS = 100
const_color = 255.99

# Image header
# P3 defines the image format.255 is maximum color value.
# nx pixel by ny pixel image
print(f"P3\n{NX} {NY}\n255")

world = HitableList([Sphere(Vector(0, 0, -1), 0.5), Sphere(Vector(0, -100.5, -1), 100)])
cam = Camera()

j = NY - 1
while j >= 0:
    for i in range(NX):
        col = Vector(0.0, 0.0, 0.0)
        for s in range(NS):
            u = float((i + random()) / NX)
            v = float((j + random()) / NY)
            r = cam.getRay(u, v)
            p = r.point_at_parameter(2.0)
            col = col + r.color(world)

        col = col.divide_scalar(float(NS))
        ir = int(const_color * (math.sqrt(col.x)))
        ig = int(const_color * (math.sqrt(col.y)))
        ib = int(const_color * (math.sqrt(col.z)))

        print(ir, ig, ib)

    j -= 1