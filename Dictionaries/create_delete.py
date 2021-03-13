#Create
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

#Print
print(inventory)
print(inventory["apples"])

#Change
inventory['pears'] = 0

print(inventory)

#Delete
del inventory['pears']

print(inventory)

#Length
print(len(inventory))