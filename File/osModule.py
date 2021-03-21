Source: https://www.geeksforgeeks.org/os-module-python-examples/



# Python program to explain os.getcwd() method  
          
# importing os module  
import os  
      
# Get the current working  
# directory (CWD)  
cwd = os.getcwd()  
      
# Print the current working  
# directory (CWD)  
print("Current working directory:", cwd)

# Python program to change the  
# current working directory  
    
    
import os  
    
# Function to Get the current   
# working directory  
def current_path():  
    print("Current working directory before")  
    print(os.getcwd())  
    print()  
    
    
# Driver's code  
# Printing CWD before  
current_path()  
    
# Changing the CWD  
os.chdir('../')  
    
# Printing CWD after  
current_path()  


# Python program to explain os.mkdir() method  
  
# importing os module  
import os  
  
# Directory  
directory = "GeeksforGeeks"
  
# Parent Directory path  
parent_dir = "D:/Pycharm projects/"
  
# Path  
path = os.path.join(parent_dir, directory)  
  
# Create the directory  
# 'GeeksForGeeks' in  
# '/home / User / Documents'  
os.mkdir(path)  
print("Directory '% s' created" % directory)  
  
# Directory  
directory = "Geeks"
  
# Parent Directory path  
parent_dir = "D:/Pycharm projects"
  
# mode  
mode = 0o666
  
# Path  
path = os.path.join(parent_dir, directory)  
  
# Create the directory  
# 'GeeksForGeeks' in  
# '/home / User / Documents'  
# with mode 0o666  
os.mkdir(path, mode)  
print("Directory '% s' created" % directory)  




# Python program to explain os.makedirs() method  
      
# importing os module  
import os  
      
# Leaf directory  
directory = "Nikhil"
      
# Parent Directories  
parent_dir = "D:/Pycharm projects/GeeksForGeeks/Authors"
      
# Path  
path = os.path.join(parent_dir, directory)  
      
# Create the directory  
# 'Nikhil'  
os.makedirs(path)  
print("Directory '% s' created" % directory)  
      
# Directory 'GeeksForGeeks' and 'Authors' will  
# be created too  
# if it does not exists  
      
      
      
# Leaf directory  
directory = "c"
      
# Parent Directories  
parent_dir = "D:/Pycharm projects/GeeksforGeeks/a/b"
      
# mode  
mode = 0o666
      
path = os.path.join(parent_dir, directory)  
      
# Create the directory 'c'  
      
os.makedirs(path, mode)  
print("Directory '% s' created" % directory)  
      
      
# 'GeeksForGeeks', 'a', and 'b'  
# will also be created if  
# it does not exists  
      
# If any of the intermediate level  
# directory is missing  
# os.makedirs() method will  
# create them  
      
# os.makedirs() method can be  
# used to create a directory tree




# Python program to explain os.listdir() method  
      
# importing os module  
import os  
  
# Get the list of all files and directories  
# in the root directory  
path = "/"
dir_list = os.listdir(path)  
  
print("Files and directories in '", path, "' :")  
  
# print the list  
print(dir_list)  




# Python program to explain os.remove() method  
      
# importing os module  
import os  
      
# File name  
file = 'file1.txt'
      
# File location  
location = "D:/Pycharm projects/GeeksforGeeks/Authors/Nikhil/"
      
# Path  
path = os.path.join(location, file)  
      
# Remove the file  
# 'file.txt'  
os.remove(path)  



# Python program to explain os.rmdir() method  
      
# importing os module  
import os  
      
# Directory name  
directory = "Geeks"
      
# Parent Directory  
parent = "D:/Pycharm projects/"
      
# Path  
path = os.path.join(parent, directory)  
      
# Remove the Directory  
# "Geeks"  
os.rmdir(path) 




import os 
  
  
try: 
    # If the file does not exist, 
    # then it would throw an IOError 
    filename = 'GFG.txt'
    f = open(filename, 'rU') 
    text = f.read() 
    f.close() 
  
# Control jumps directly to here if  
# any of the above lines throws IOError.     
except IOError: 
  
    # print(os.error) will <class 'OSError'> 
    print('Problem reading: ' + filename) 
      
# In any case, the code then continues with  
# the line after the try/except 





import os 
fd = "GFG.txt"
  
# popen() is similar to open() 
file = open(fd, 'w') 
file.write("Hello") 
file.close() 
file = open(fd, 'r') 
text = file.read() 
print(text) 
  
# popen() provides a pipe/gateway and accesses the file directly 
file = os.popen(fd, 'w') 
file.write("Hello") 
# File not closed, shown in next function. 


import os 

fd = "GFG.txt"
file = open(fd, 'r') 
text = file.read() 
print(text) 
os.close(file) 




import os 
  
  
fd = "GFG.txt"
os.rename(fd,'New.txt') 
os.rename(fd,'New.txt') #this will not work as fd is renamed now.



