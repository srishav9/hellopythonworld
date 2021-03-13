f = open('NOTE.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
letter_counts = {} # start with an empty dictionary
for c in txt:
    if c not in letter_counts:
        # we have not seen this character before, so initialize a counter for it
        letter_counts[c] = 0
    #whether we've seen it before or not, increment its counter
    letter_counts[c] = letter_counts[c] + 1
for c in letter_counts.keys():
    print(c + ": " + str(letter_counts[c]) + " occurrences")

#Version 2.0
x = input("Enter a sentence")
x = x.lower()   # convert to all lowercase
alphabet = 'abcdefghijklmnopqrstuvwxyz'
letter_count = {} # empty dictionary
for char in x:
    if char in alphabet: # ignore any punctuation, numbers, etc
        if char in letter_count:
            letter_count[char] = letter_count[char] + 1
        else:
            letter_count[char] = 1
keys = letter_count.keys()
for char in sorted(list(keys)):
    print(char, letter_count[char])

