import Image

im = Image.open("amy_sheldon.jpg")

# Set the upper left corners of the Amy and Sheldon regions
# Set a fixed height and width
amy_x = 110
amy_y = 105
sheldon_x = 445
sheldon_y = 40
w = 100
h = 100

# Crop out and reflect Amy's and Sheldon's heads
sheldon_head = im.crop((sheldon_x, sheldon_y, sheldon_x+w, sheldon_y+h))
sheldon_reflected = sheldon_head.transpose(Image.FLIP_LEFT_RIGHT)
amy_head = im.crop((amy_x,amy_y, amy_x+w, amy_y+h))
amy_reflected = amy_head.transpose(Image.FLIP_LEFT_RIGHT)

# Paste the regions back into the image and show it
im.paste(sheldon_reflected, (amy_x,amy_y))
im.paste(amy_reflected, (sheldon_x,sheldon_y))
im.show()
