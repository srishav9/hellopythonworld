#count_lines

f=open("travel_plans2.txt")
num_lines=0
for line in f:
    num_lines+=1
print(num_lines)