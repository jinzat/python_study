'''count prime number'''
for i in range (2,101):
    k=0
    for j in range (2,i-1):
        if i%j==0:
            k=1
           
        elif k==0:
            print(i)
   
    
