import os

from PIL import Image

#taking pictures of my harddrive, must be changed soon
pictures = os.listdir (r"C:\Users\makeda\programming\catapop\images")

file_currently_reading = 0
file_number_count = len(pictures)
 
while file_currently_reading < file_number_count:
    filename = pictures[file_currently_reading]

    im = Image.open(r"C:\Users\makeda\programming\catapop\images\\" + filename)
  ## do some basic matrix math
    im= im.transform(im.size, Image.AFFINE, [1,-0.0018, -20,0.039,1.0337,-20],resample=Image.BICUBIC)
    
    ## add noise- add a nother line of code for that below
    ##-#pending, must check PIL documentation
    
    
    ##saveoutput
    im.save(r"C:\Users\makeda\programming\catapop\images\transformed\\"+filename,"PNG")
        
    file_currently_reading =    file_currently_reading +1
    
