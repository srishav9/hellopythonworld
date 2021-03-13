print("#KEYS - returns list of keys")
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

for akey in inventory.keys():     # the order in which we get the keys is not defined
    print("Got key", akey, "which maps to value", inventory[akey])

ks = list(inventory.keys())
print(ks)

print("#inShort as for loop implicitly takes in keys as a list:")
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

for k in inventory:
    print("Got key", k)


print("#VALUES - return list of values")
print("#ITEMS - returns tuples(key,value) in dictionary")
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print(".values():",list(inventory.values()))
print(".items():",list(inventory.items()))
for k in inventory:
    print("Got",k,"that maps to",inventory[k])


print("The in and not in operators can test if a key is in the dictionary:")
print("This operator can be very useful since looking up a non-existent key in a dictionary causes a runtime error.")
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print('apples' in inventory)
print('cherries' in inventory)

if 'bananas' in inventory:
    print(inventory['bananas'])
else:
    print("We have no bananas")


#Get:
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print(inventory.get("apples"))
print(inventory.get("cherries"))
print(inventory.get("cherries",0))