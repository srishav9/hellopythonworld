#Files IN Python:
#as usual:
#FILE <-----> Descriptor <------> PYTHON

file_path = "travel_plans2.txt"

# try:
#     fhand = open(file_path)
# except:
#     print("File not found!!", end=" ")
#     quit()
# print(fhand.read()) #prints whole file as STRING
# fhand.close()

try:
    fhand = open(file_path)
except:
    print("\n ****File not found****")
    quit()
stri = fhand.read()
print(stri.split())
"""        ^ will give all the words in the file in a list,
strip without any parameter will strip out all the witespaces and \n's and \t's


and BTW this is Mutiline Comment in Python
"""
fhand.close()

'''

file descriptor functions:

read()      --> returns whole file as a single string
readline()  --> returns line-wise strings
readlines() --> returns whole file as a line-wise list

'''