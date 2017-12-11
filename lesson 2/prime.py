'''count prime number'''
while i in range (1,51):
    
    a=(2**i-2)/i
    b=a//1
    c=i
    
    if (a==b):
        print(c)

        for m in range (51,101):
            if m%c!=0:
                print (m)
    
