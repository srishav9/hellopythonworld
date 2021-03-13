sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
sentence=sentence.split()
word_counts = {} # start with an empty dictionary
for c in sentence:
    if c not in word_counts:
        # we have not seen this character before, so initialize a counter for it
        word_counts[c] = 0
    #whether we've seen it before or not, increment its counter
    word_counts[c] = word_counts[c] + 1
for c in word_counts.keys():
    print(c + ": " + str(word_counts[c]) + " occurrences")

