#program to remove ifunny watermark
#page 393 automating
import os
from pathlib import Path
from PIL import Image

startFolder = Path.cwd()/"Original"

def crop(image, count):
    imageExt = os.path.splitext(image)[-1].lower()
    originalImage = Image.open(image)
    width, height = originalImage.size
    croppedImage = originalImage.crop((0, 0, width, (height-21)))
    croppedName = str(count) + imageExt
    croppedImage.save(Path.cwd()/"Cropped"/croppedName)

o = os.listdir(startFolder)
count = 0                  #creates list of all files in starting folder
for x in range(len(o)):
	image = o[x]
	print (startFolder/image)
	crop(startFolder/image, x)