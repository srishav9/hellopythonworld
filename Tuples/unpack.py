
pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}
#unpacking automatically using for:
for k,v in pokemon.items():
    print("Key: {}, Value: {}".format(k,v))


#unpacking in a function:
def add(x, y):
    return x + y

print(add(3, 4))
z = (5, 4)
print(add(*z)) # this line will cause the values to be unpacked
