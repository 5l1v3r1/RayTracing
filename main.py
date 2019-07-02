from vector import Vector

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
		# red and green values range from 0.0 to 1.0
		v = Vector(float(i/nx),float(j/ny),0.2)
		ir = int(const*v.X)
		ig = int(const*v.Y)
		ib = int(const*v.Z)
		print(ir, ig, ib)       
	j-=1   
