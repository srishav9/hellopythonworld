import os
import shutil
from os.path import isfile
#print(dir(os)) #list all items
#print(os.name) #nt
#print(os.__doc__) #help document
#print(os.listdir())
l = os.listdir('.')
dest="D:\\Coding\\codes\\Qt-Tutorials\\all\\"
d={}
ll=[]
rmv="readme.txt"
for el in l:
    if not isfile(el):
        if el == "all": continue
        os.chdir(el)
        p=os.getcwd().split('\\')
        #print(os.getcwd(),rmv,"  ",dest)
        #print(dest+"\\"+rmv)
        # shutil.move(rmv,dest)
        # os.remove(dest+"\\"+rmv)
        d[p.pop()]=os.listdir()
        #print(os.listdir())
        os.chdir("\\".join(p))
#print(d)
for k in d:
    if k[0] == "Q":
        ll.append(int(k.split("-")[1]))     #Qt-33 name
for i in sorted(ll):
    #if d["Qt-"+str(i)] == []:
        #print("Qt-"+str(i), d["Qt-"+str(i)])
        #print("Qt-"+str(i), end=" ")
    if len(d["Qt-"+str(i)]) == 1:
        print("Qt-"+str(i), end=" ")
