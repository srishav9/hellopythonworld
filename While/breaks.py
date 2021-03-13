# a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).

def sublist(nums):
    i=0
    num=list()
    while(True):
        if nums[i]!=5:
            num.append(nums[i])
        else:
            break
        i += 1
        if i >= len(nums):
            break
    return num

sublist([1,2,3,4,5,6,7,8])
sublist([5])
sublist([8,6,5])
sublist([1,6,2,3,9])
