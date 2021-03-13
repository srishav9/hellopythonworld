#
# sum1 = 0
# sum2 = 0
# lst = [65, 78, 21, 33]
#
# for x in lst:
#     sum1 = sum1 + x
# i=0
# while(i<len(lst)):
#     sum2 += lst[i]
#     i+=1
# if sum1==sum2:
#     print("SUCCESS!!")

def test(x,y=True,z={2:3, 4:5, 6:8}):
    if y==True:
        if x in list(z.keys()):
            return z[x]
    else:
        return False

test(2)
test(4,False)
test()
