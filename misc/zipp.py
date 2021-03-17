print("""ZIP(Pair-wise operations):
Takes multiple lists and turns them into a list of tuples
(actually, an iterator, but they work like lists for most practical purposes),
pairing up all the first items as one tuple, all the second items as a tuple, and so on.
""")

L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = []
for i in range(len(L1)):
    L3.append(L1[i] + L2[i])
print(L3)

L3.clear()  # removes all items from alist (equivalent to del alist[:])
"""
dont just do:
    alist=[] as it does not empty the list,
    just creates a new object and binds it to the variable lst,
    but the old list will still have the same elements,
    and effect will be apparent if it had other variable bindings.
Best ways:
    alist.clear()   # Python 3.3+
    del alist[:]
    alist[:] = []   #slowest as iterating and clearing
    alist *= 0
"""
print("---------------------")
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L4 = list(zip(L1, L2))
print("{}\n{}\n{}".format(L1,L2,L4))
for (x1, x2) in L4:
    L3.append(x1+x2)
print(L3)
print("map")
print(list(map(lambda x: x[0] + x[1], zip(L1, L2))))
print('list comp')
print([x+y for x,y in L4])



print("---------------------------------------------------------------")
def possible(word, blanked, guesses_made):
    if len(word) != len(blanked):
        return False
    for i in range(len(word)):
        bc = blanked[i]
        wc = word[i]
        if bc == '_' and wc in guesses_made:
            return False
        elif bc != '_' and bc != wc:
            return False
    return True

print(possible("wonderwall", "_on__r__ll", "otnqurl"))
print(possible("wonderwall", "_on__r__ll", "wotnqurl"))

#using zip
def possible(word, blanked, guesses_made):
    if len(word) != len(blanked):
        return False
    for (bc, wc) in zip(blanked, word):
        if bc == '_' and wc in guesses_made:
            return False
        elif bc != '_' and bc != wc:
            return False
    return True

print(possible("wonderwall", "_on__r__ll", "otnqurl"))
print(possible("wonderwall", "_on__r__ll", "wotnqurl"))
