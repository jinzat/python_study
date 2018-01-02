from scipy.misc import imread
import matplotlib.pyplot as plt

img=imread('lena.png') #导入图片路径
w,h=img.shape[:2]#取得行和列
img[:w//2,:h//2]=(255,0,0)# 給某一块图片上色，利用切片
plt.imshow(img)
plt.show
