
#moving empty directories to a location and then deleting them later

import os
import shutil
str = 'Qt-143 Qt-144 Qt-145 Qt-146 Qt-147 Qt-152' #empty directories
lst = str.split()
os.chdir('D:\\Qt-Tutorials\\all')
dest="D:\\Qt-Tutorials\\all\\rmv\\"
for x in lst:
    #print("D:\Coding\codes\Qt-Tutorials"+"\\"+x+"\\")
    #os.remove("D:\\Coding\\codes\\Qt-Tutorials"+"\\"+rm)
    #os.chdir(x)
    #y=f"D:\\Coding\\codes\\Qt-Tutorials\\all\\{x}\\"+os.listdir()[0]
    #print(x,end=" ")
    #shutil.move("D:\Coding\codes\Qt-Tutorials\\all"+"\\"+x,dest)
    #os.chdir('D:\Coding\codes\Qt-Tutorials\\all')
