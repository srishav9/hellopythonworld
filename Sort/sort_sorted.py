print("Using sort()")
L1=[5,4,2,8,9,-1,-10]
print("L1 before:",L1)
L2=["Cherry","Strawberry","Watermelon","Banana","Apple"]
print("L2 before:",L2)
L1.sort()
print("L1:",L1)
L2.sort()
print("L2:",L2)

print("Using sorted().. Original LIST is UNchanged")
L1=[5,4,2,8,9,-1,-10]
L2=["Cherry","Strawberry","Watermelon","Banana","Apple"]
L3=sorted(L1)
print("L1:",L1)
print("L3:",L3)
L4=sorted(L2)
print("L2:",L2)
print("L4:",L4)
print("Reverse sort using sorted(list,reverse=True)")
print(sorted(L1,reverse=True))
print("Absolute sort using sorted(list,key=absolute) after defining the absolute function")
print("THE VALUE PASSED TO THE KEY PARAMETER HAS TO BE A FUNCTION")
def absolute(x):
    if x >=0 :
        return x
    else:
        return -x
print(sorted(L1,key=absolute))
print(sorted(L1,reverse=True,key=lambda x:absolute(x)))
