import numpy as np
from PIL import Image

png_input1 = './scrambled1.png'
png_input2 = './scrambled2.png'
png_output = 'ans.png'

im1 = np.array(Image.open(png_input1))
im2 = np.array(Image.open(png_input2))

im1.shape, im2.shape

Image.fromarray(im1 + im2).save(png_output)
