from vector import Vector
from ray import Ray

nx = 200
ny = 100
const = 255.99

#Image header
#P3 defines the image format.
#255 is maximum color value.
#nx pixel by ny pixel image
print(f"P3\n{nx} {ny}\n255")

lowerLeft = Vector(-2.0, -1.0, -1.0)
horizontal = Vector(4.0, 0.0, 0.0)
vertical = Vector(0.0, 2.0, 0.0)
origin = Vector(0.0, 0.0, 0.0)

j = ny-1

while(j >= 0):
    for i in range(nx):
        u = float(i/nx)
        v = float(j/ny)
    
        hor = horizontal.multiplyScalar(u)
        vert = vertical.multiplyScalar(v)

        v1 = hor.add(vert)
        v2 = lowerLeft.add(v1)
        direction = v1.add(v2)

        r = Ray(origin, direction)
        rgb = r.color()
           
        ir = int(const*rgb.X)
        ig = int(const*rgb.Y)
        ib = int(const*rgb.Z)
        print(ir, ig, ib)
    j-=1