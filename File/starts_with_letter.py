fname = "filename.txt"
j_file=list()
with open(fname, 'r') as fileref:         # step 1
    for line in fileref:
        line=line.rstrip().split()
        for word in line:
            if word.startswith("j"): j_file.append(word)
print(j_file)