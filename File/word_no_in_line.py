#get third word in every line
f=open("school_prompt.txt")
three=list()
for line in f:
    line=line.rstrip().split()
    three.append(line[2])
print(three)