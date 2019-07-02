nx = 200
ny = 100
const = 255.99

#Image header
#P3 defines the image format.
#255 is maximum color value.
#nx pixel by ny pixel image
print(f"P3\n{nx} {ny}\n255")

j = ny-1
while(j>=0):
    for i in range(nx):
        r = float(i/nx)
        g = float(j/ny)
        b = 0.2
        ir = int(const*r)
        ig = int(const*g)
        ib = int(const*b)
        print(ir, ig, ib)       
    j=j-1