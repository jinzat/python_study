from scipy.misc import imread
import matplotlib.pyplot as plt
import numpy as np
img=imread('lena.png') #导入图片路径
img=imread('lena.png', True)
hist,bins=np.histogram (img,256,(0,256))#对直方图统计用bins投票


'''
print(hist)
plt.imshow(img,cmap='gray')#以灰度形式读出来
plt.plot(hist)
plt.show()
'''


