import numpy as np
from PIL import Image

png_input1 = './share1.png'
png_input2 = './share2.png'
png_output1 = 'ans1.png'

im1 = np.array(Image.open(png_input1))
im2 = np.array(Image.open(png_input2))

print(im1.shape, im2.shape)

Image.fromarray(im1 ^ im2).save(png_output1)

png_input3 = './secret.zip'
png_output2 = 'ans2.png'
im3 = np.array(Image.open(png_input3))
print(im1.shape, im2.shape, im3.shape)
Image.fromarray(im1 ^ im2 ^ im3).save(png_output2)
