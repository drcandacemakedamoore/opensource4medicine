#this only runs through images, does not ,multiply the matrix to augment data
# to augment data use code in synthrad folder- multiply the matrix as in that code
import numpy as np
import os
import PIL
from PIL import Image
# first get the images down to arrays
pictures = os.listdir (r"C:\Users\makeda\programming\catapop\images")

file_currently_reading = 0
file_number_count = len(pictures)
 
while file_currently_reading < file_number_count:
    filename = pictures[file_currently_reading]

    im = Image.open(r"C:\Users\makeda\programming\catapop\images\\" + filename)
    tuples=im.split()
    second_element_of_tuple=tuples[1]    


    image_string = np.asarray(second_element_of_tuple)    
    pastetodoc = open('list_of_png_as_array.bin','a')
    pastetodoc.write(np.array2string(image_string))        
  
                 
file_currently_reading = file_currently_reading +1
# then perform all kinds of operations on these arrays- paste all tested ones here 
