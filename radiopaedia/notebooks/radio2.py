##Radiopaedia Code Sandbox for making augmented data



import os
import numpy as np
from skimage.data import shepp_logan_phantom
from PIL import Image, ImageFilter


def show(img, cmap=None):
    cmap = cmap or plt.cm.gray
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.imshow(img, cmap=cmap)
    ax.set_aRadiopaedia Code Sandbox for making augmented dataxis_off()
    plt.show()

im = shepp_logan_phantom
  ## do some basic matrix math 

#show me the basic image here- a phantom for the head

show(img)

#to scew it
    im= im.transform(im.size, Image.AFFINE, [1,-0.0018, -20,0.039,1.0337,-20],resample=Image.BICUBIC)
  ## add a gaussian filter -add noise based on a standard deviation + mean *needs a better explanation
    im_gauss= im.filter(ImageFilter.GaussianBlur(1))
##boxblur- add an explantion
    im_otherfilter =im.filter(ImageFilter.BoxBlur(3))

   
