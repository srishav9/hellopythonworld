#Note Using access() to check if a user is authorized to e.g. open a file before actually doing so using open() creates a security hole, 
#because the user might exploit the short time interval between checking and opening the file to manipulate it. 
#It’s preferable to use EAFP techniques. For example:

if os.access("myfile", os.R_OK):
    with open("myfile") as fp:
        return fp.read()
return "some default data"

#is better written as:

try:
    fp = open("myfile")
except PermissionError:
    return "some default data"
else:
    with fp:
        return fp.read()
