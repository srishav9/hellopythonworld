filename = "squared_numbers.txt"
outfile = open(filename, "w")

for number in range(1, 13):
    square = number * number
    outfile.write(str(square) + "\n")

outfile.close()

infile = open(filename, "r")
print(infile.read()[:10])
infile.close()

#CSV format files => Comma Separated Files, they are easy to put in Excel sheets.
#Example:
# Name,score,grade
# Jamal,98,A+
# Eloise,87,B+
# Madeline,99,A+
# Wei,94,A