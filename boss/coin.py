import numpy as np
from skimage.data import coins
from skimage import feature
import matplotlib.pyplot as plt
from scipy.ndimage import center_of_mass,filters,morphology,binary_closing,binary_dilation,binary_opening,binary_erosion

img=coins()

plt.imshow(img, cmap='gray')
plt.figure()


edges=feature.canny(img,sigma=3)# canny to take the edge

img1=binary_dilation(edges)
img2=morphology.binary_fill_holes(img1)
img3=binary_erosion(img2)

img5=filters.gaussian_filter(img3,sigma=1)

# center_of_mass()
plt.imshow(img5)
plt.show()



