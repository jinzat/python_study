import os #os module
f=open('namelist.txt')# open the name file
ls=f.readline()[-2] # make a list,[-1]dele /n
f.close()
for i in ls: print (i)
    name=i.split('/')[-2])
    os.mkdir(name)#create fordername based on the address
    os.system('git clone %s %s'%(i+'.git',name)
    

