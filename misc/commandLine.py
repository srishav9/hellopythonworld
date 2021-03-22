# Command-Line Arguments and Exit Status
import sys
print(sys.argv)

import os

# Receives a file name as a command line argument
filename = sys.argv[0]

# Checks whether the file name exist or not
# When the file doesn't exist, it creates it by writing a line to it
if not os.path.exists(filename):
     with open(filename, "w") as f:
         f.write("New file created\n")
# When the file exist, our script print an error message and exits with an exit value of one
else:
    print("Error, the file {} already exists!".format(filename))
    sys.exit(1)
