def last_four(x):
    num=list()
    while(x!=0):
        n=x%10
        x=int(x/10)
        num.insert(0,n)
    num=num[-len(num)+4:]
    ret=""
    for i in range(4):
        ret=ret+str(num[i])
    return ret

sorted_ids=list()
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
for id in ids:
    sorted_ids.append(last_four(id))
sorted_i=sorted(ids,key=last_four)
print(sorted_i)
sorted_ids=sorted_i

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
for i in range(len(ids)):
    ids[i]=str(ids[i])
sorted_id=sorted(ids,key=lambda id:id[-4:])
for i in range(len(sorted_id)):
    sorted_id[i]=int(sorted_id[i])
