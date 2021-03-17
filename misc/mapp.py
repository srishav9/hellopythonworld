print('#MAP fn TRANSFORMS TO NEW FORM')


def triple(value):
    return 3*value

def tripleStuff(a_list):
    new_seq = map(triple, a_list)
    return list(new_seq)

def quadrupleStuff(a_list):
    new_seq = map(lambda value: 4*value, a_list)
    return list(new_seq)

things = [2, 5, 9]
things3 = tripleStuff(things)
print(things3)
things4 = quadrupleStuff(things)
print(things4)


things = [2, 5, 9]

things4 = map((lambda value: 4*value), things)
print(list(things4))

# or all on one line
print(list(map((lambda value: 5*value), [1, 2, 3])))

abbrevs = ["ind", "usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]
abbrevs_upper=list(map((lambda x: x.upper()), abbrevs))
print(abbrevs_upper)
