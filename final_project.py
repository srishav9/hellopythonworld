punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(word):
    for ch in word:
        if ch in punctuation_chars:
            word=word.replace(ch,"")
    return word

# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(strings):
    count = 0
    str_l=strings.split()
    for string in str_l:
        string=strip_punctuation(string).lower()
        if string in positive_words:
            count += 1
    return count

# list of negative words to use
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(strings):
    count = 0
    str_l=strings.split()
    for string in str_l:
        string=strip_punctuation(string).lower()
        if string in negative_words:
            count += 1
    return count

fc = open("project_twitter_data.csv", 'r')
fh = open("resulting_data.csv", "w")
lines = fc.readlines()
header = lines[0]
field_names = header.strip().split(',')
fh.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
fh.write('\n')
for row in lines[1:]:
    vals = row.strip().split(',')
    if len(vals)<3:
        continue
    pos_words=get_pos(vals[0])
    neg_words=get_neg(vals[0])
    net_score=pos_words-neg_words
    row_string = '{},{},{},{},{}'.format(vals[1], vals[2], pos_words, neg_words, net_score)
    fh.write(row_string+'\n')
fc.close()
fh.close()
