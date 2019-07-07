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

j = ny - 1

while(j >= 0):
    for i in range(nx):
        u = float(i / nx)
        v = float(j / ny)
    
        hor = horizontal.multiplyScalar(u)
        vert = vertical.multiplyScalar(v)

        v1 = hor + vert
        v2 = lowerLeft + v1
        direction = v1 + v2

        rgb = Ray(origin,direction).color()
                
        ir = int(const*rgb.x)
        ig = int(const*rgb.y)
        ib = int(const*rgb.z)

        print(ir, ig, ib)  
           
    j-=1