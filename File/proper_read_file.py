fname = "yourfile.txt"
with open(fname, 'r') as fileref:         # step 1
    lines = fileref.readlines()           # step 2
    for lin in lines:                     # step 3
        pass
        #some code that references the variable lin
#some other code not relying on fileref   # step 4


# However, this will not be good to use when you are working with large data. Imagine working with a datafile that has 1000 rows of data. 
# It would take a long time to read in all the data and then if you had to iterate over it, even more time would be necessary. 
# This would be a case where programmers prefer another option for efficiency reasons.

# This option involves iterating over the file itself while still iterating over each line in the file:


fname = "yourfile.txt"
with open(fname, 'r') as fileref:         # step 1
    for line in fileref:                   # step 2
        print(line)
        ## some code that reference the variable lin
#some other code not relying on fileref   # step 3
