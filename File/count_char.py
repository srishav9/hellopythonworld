#char_count
f=open("school_prompt2.txt")
count=0
for c in f:
#    c=c.rstrip()
#    c=c.split()
    for x in c:
        for y in x:
            #if(y=="." or y==","): continue
            count+=1
num_char=count
print(num_char)


# #SIMPLE VERSION
# f=open("school_prompt2.txt")
# num_char=0
# for c in f:
#     for x in c:
#         for y in x:
#             num_char+=1
# print(num_char)