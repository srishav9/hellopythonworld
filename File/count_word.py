f=open("emotion_words.txt")
count=0
for line in f:
    line=line.rstrip().split()
    for word in line:
        count+=1
num_words=count
print(num_words)