fname = "school_prompt.txt"
p_words=list()
with open(fname, 'r') as fileref:
    for line in fileref:
        line=line.rstrip().split()
        for word in line:
            if "p" in word: p_words.append(word)
print(p_words)