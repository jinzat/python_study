import numpy as np
from skimage.data import coins
import matplotlib.pyplot as plt
from scipy.ndimage import uniform_filter,gaussian_filter,sobel,uniform_filter

img=coins()
'''
plt.imshow(img, cmap='gray')
plt.figure()
'''
img1=(img-img.min())/(img.max()-img.min())*255
'''
img1=gaussian_filter(img,7)
'''
plt.imshow(img1, cmap='gray')
'''
hist,bin=np.histogram (img1,256,(0,256))#7-54.39
plt.plot(hist)
'''

img3=gaussian_filter(img1,5)
plt.imshow(img3>120, cmap='gray')
plt.show ()#8-32.41

    

