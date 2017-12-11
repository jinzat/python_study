'''裴波那挈数列'''
a=0
b=1 # a 为 0 b 为 1
i=1
c=0
while i in range (0,101):
    print('a',a,'b',b)
    c=b
    b=a+b
    a=c
    i=i+1

    if (i==99): #输出第99项
       c=b
    if (i==100):#输出第100项
        d=b

m=d/c
print(m) # 第100项和第99项比值



        
       
