n=int(input('找出0-n之间的质数为n大于等于2的整数，输入n='))
s1=set([i for i in range (2,n+1)])
s2=set([x*y for x in range(2,n+1) for y in range(2,x+1)])
print(s1-s2)#'质数'
'''
print(s1)#'数集'
print(s2)#'合数'
'''
