from hitableList import HitableList
from sphere import Sphere
from vector import Vector
from camera import Camera
from ray import Ray

import random

nx = 200
ny = 100
ns = 100
const = 255.99

#Image header
#P3 defines the image format.255 is maximum color value.
#nx pixel by ny pixel image
print(f"P3\n{nx} {ny}\n255")

lowerLeft = Vector(-2.0, -1.0, -1.0)
horizontal = Vector(4.0, 0.0, 0.0)
vertical = Vector(0.0, 2.0, 0.0)
origin = Vector(0.0, 0.0, 0.0)

world = HitableList([
    Sphere(Vector(0, 0, -1), 0.5),
    Sphere(Vector(0, -100.5, -1), 100)
])

cam = Camera()

j = ny - 1
while(j >= 0):
    for i in range(nx):
        col = Vector(0.0, 0.0,0.0)
        for s in range(ns):
            u = float((i + random.uniform(0, 1)) / nx)
            v = float((j + random.uniform(0,1)) / ny)
            r = cam.getRay(u,v)
            p = r.pointAtParameter(2.0)
            col = col + r.color(world)
        
        col = col.divideScalar(float(ns))               
        ir = int(const*col.x)
        ig = int(const*col.y)
        ib = int(const*col.z)

        print(ir, ig, ib)  
           
    j-=1