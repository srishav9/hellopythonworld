fileconnection = open("olympics.txt", 'r')
lines = fileconnection.readlines()
header = lines[0]
field_names = header.strip().split(',')
print(field_names)
for row in lines[1:]:
    vals = row.strip().split(',')
    print(vals)
    if len(vals) < 2 or vals[5] == "NA":	continue
    print("{}: {}; {}".format(
    vals[0],
    vals[4],
    vals[5]))
