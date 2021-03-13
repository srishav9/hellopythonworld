#Accumulator variable strategy

fh = open('NOTE.txt', 'r')
txt = fh.read()
# now txt is one long string containing all the characters
i_count = 0 #initialize the accumulator variable
t_count = 0 #initialize the accumulator variable
s_count = 0 # initialize the s counter accumulator as well
for c in txt:
    if c == 'i':
        i_count = i_count + 1   #increment the counter
    if c == 't':
        t_count = t_count + 1   #increment the t counter
    elif c == 's':
        s_count = s_count + 1
print("i: " + str(i_count) + " occurrences")
print("t: " + str(t_count) + " occurrences")
print("s: " + str(s_count) + " occurrences")


#Dictionary variable strategy

f = open('NOTE.txt', 'r')
txt = f.read()
x = {} # start with an empty dictionary
x['t'] = 0  # initialize the t counter
x['s'] = 0  # initialize the s counter
for c in txt:
    if c == 't':
        x['t'] = x['t'] + 1  # increment the t counter
    elif c == 's':
        x['s'] = x['s'] + 1  # increment the s counter
print("t: " + str(x['t']) + " occurrences")
print("s: " + str(x['s']) + " occurrences")


#Looking closely the above code:
#Whichever character we’re seeing, t or s, we’re incrementing the counter for that character.
f = open('NOTE.txt', 'r')
txt = f.read()
x = {} # start with an empty dictionary
x['t'] = 0  # intiialize the t counter
x['s'] = 0  # initialize the s counter
for c in txt:
    if c == 't':
        x[c] = x[c] + 1   # increment the t counter
    elif c == 's':
        x[c] = x[c] + 1   # increment the s counter
print("t: " + str(x['t']) + " occurrences")
print("s: " + str(x['s']) + " occurrences")


#We can still do better:

f = open('NOTE.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
x = {} # start with an empty dictionary
for c in txt:
    if c not in x:
        # we have not seen this character before, so initialize a counter for it
        x[c] = 0
    #whether we've seen it before or not, increment its counter
    x[c] = x[c] + 1
print("t: " + str(x['t']) + " occurrences")
print("s: " + str(x['s']) + " occurrences")


#Even better :
#We can generalize that, too, to print out the occurrence counts for all of the characters,
#using a for loop to iterate through the keys in x.
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