def fib_lst(lim,lst=[],a=1,b=0,lev=1):
    lst.append(a+b)
    if lev == lim:return lst
    a,b=b,a+b
    return fib_lst(lim,lst,a,b,lev+1)

print(fib_lst(5))

