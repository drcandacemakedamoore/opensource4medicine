import os

from PIL import Image


pictures = os.listdir (r"C:\Users\makeda\programming\catapop\images")

file_currently_reading = 0
file_number_count = len(pictures)
 
while file_currently_reading < file_number_count:
    filename = pictures[file_currently_reading]

    im = Image.open(r"C:\Users\makeda\programming\catapop\images\\" + filename)
  
    im= im.transform(im.size, Image.AFFINE, [1,-0.0018, -20,0.039,1.0337,-20],resample=Image.BICUBIC)
    im.save(r"C:\Users\makeda\programming\catapop\images\transformed\\"+filename,"PNG")
        
    file_currently_reading =    file_currently_reading +1
    



