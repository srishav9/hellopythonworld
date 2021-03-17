print('#FILTER fn GENERATES A DECISION')


print("Functions")
def keep_evens(nums):
    new_list = []
    for num in nums:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

print(keep_evens([3, 4, 6, 7, 0, 1]))

print("FILTER")
def keep_evens(nums):
    new_seq = filter(lambda num: num % 2 == 0, nums)
    return list(new_seq)

print(keep_evens([3, 4, 6, 7, 0, 1]))


lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

def keep_evens(nums):
    new_seq = filter(lambda num: 'w' in num, nums)
    return list(new_seq)

filter_testing = keep_evens(lst_check)
print(filter_testing)
