'''
Created on Sep 17, 2013

@author: hsartoris
'''

from PIL import Image


cuoco = Image.open("Cuoco.jpg")
parsons = Image.open("Parsons.jpg")

cropped = cuoco.crop((95, 20, 450, 470))
cuoco = cropped.resize((200,275))

cropped = parsons.crop((95, 20, 325, 390))
parsons = cropped.resize((200,275))

for i in range(0,11):
    Image.blend(cuoco, parsons, (i / 10.0)).show()