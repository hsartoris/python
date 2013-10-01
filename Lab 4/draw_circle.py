import math
def center_distance(x0, y0, x1, y1):
    return math.sqrt((x0 - x1)**2 + (y0 - y1)**2)

from PIL import Image
from PIL import ImageDraw
from array import array

im = Image.open("birds.jpg")

# Create an object that will draw on top of the image
draw = ImageDraw.Draw(im)

# Compute the center of the image.  To do this, note that 
#   im.size(0) is the width in pixels
#   im.size(1) is the height  in pixels
xc = im.size[0]/2
yc = im.size[1]/2

print "Enter a coordinate pair inside (" + str(im.size[0]) + ", " + str(im.size[1]) + ")"
x = int(raw_input("x: "))
y = int(raw_input("y: "))

radius = float(raw_input("Enter the radius of the circle: "))
print "Enter the color code: "
r = int(raw_input("R: "))
g = int(raw_input("G: "))
b = int(raw_input("B: "))

# The drawing object has a method called "ellipse" that draws the ellipse
# that fits into the given rectangle.   By making the rectangle a square,
# we get a circle, in this case, a red one
pigRadius = 12

pigX = array('i', [375, 433, 471, 535])
pigY = array('i', [160, 156, 156, 170])

intersectCount = 0

for i in range(0,4):
    if center_distance(x, y, pigX[i], pigY[i]) <= (pigRadius + radius):
        draw.ellipse((pigX[i] - pigRadius, pigY[i] - pigRadius, pigX[i] + pigRadius, pigY[i] + pigRadius), fill = (0, 0, 0))
        intersectCount += 1

print "Intersections: " + str(intersectCount)
if intersectCount == 0:
    x0 = x - radius
    y0 = y - radius
    x1 = x + radius
    y1 = y + radius
    draw.ellipse(  (x0, y0, x1, y1),  fill = (r,g,b)  )

# Show the image.  Don't forget to close the image display
# before running the program again.
im.show()
im.save("birds-circle.jpg")  # saving probably isn't necessary here....

