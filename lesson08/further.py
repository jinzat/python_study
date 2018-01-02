from scipy.misc import imread
import matplotlib.pyplot as plt

img=imread('lena.png') #导入图片路径
w,h=img.shape[:2]#取得行和列
img[:w//2,:h//2]=(255,0,0)# 給某一块图片上色，利用切片
plt.imshow(img)
plt.show ()

plt.imshow(img[::2,:,:])#利用切片第一个维度行，每两行要一行
plt.show()


plt.show(255-img)#unint8，所以要反转所有颜色及每一个通道颜色都是255与原来颜色的差值
plt.show()
