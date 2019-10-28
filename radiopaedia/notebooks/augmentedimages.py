

import os
import numpy as np
#import cv2
from PIL import Image, ImageFilter

#taking pictures of my harddrive, must be changed soon
pictures = os.listdir (r"C:\Users\makeda\programming\catapop\pimages")




file_currently_reading = 0
file_number_count = len(pictures)

 
while file_currently_reading < file_number_count:
    filename = pictures[file_currently_reading]

    im = Image.open(r"C:\Users\makeda\programming\catapop\pimages\\" + filename)
  ## do some basic matrix math to scew it
    im= im.transform(im.size, Image.AFFINE, [1,-0.0018, -20,0.039,1.0337,-20],resample=Image.BICUBIC)
  ## add a gaussian filter -add noise based on a standard deviation + mean *needs a better explanation
    im_gauss= im.filter(ImageFilter.GaussianBlur(1))
##boxblur- add an explantion
    im_otherfilter =im.filter(ImageFilter.BoxBlur(3))

    im.save(r"C:\Users\makeda\programming\catapop\images\transformed\\"+filename,"PNG")
  #  make_it_noisy(im) = im_gauss
    im_gauss.save(r"C:\Users\makeda\programming\catapop\images\transformedgaussian\\"+filename,"PNG")
    im_otherfilter.save(r"C:\Users\makeda\programming\catapop\images\otherfilter\\"+filename,"PNG")    
    file_currently_reading =    file_currently_reading +1






