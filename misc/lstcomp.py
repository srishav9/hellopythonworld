#list comprehension:
print("[<transformer_expression> for <loop_var> in <sequence> if <filtration_expression>]")

things = [2, 5, 9]
yourlist = [value * 2 for value in things]
print(yourlist)

def keep_evens(nums):
    new_list = [num for num in nums if num % 2 == 0]
    return new_list
print(keep_evens([3, 4, 6, 7, 0, 1]))


things = [3, 4, 6, 7, 0, 1]
#chaining together filter and map:
# first, filter to keep only the even numbers
# double each of them
print(map(lambda x: x*2, filter(lambda y: y % 2 == 0, things)))
# equivalent version using list comprehension
print([x*2 for x in things if x % 2 == 0])



tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},
                   {'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'},
                   {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'},
                   {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'},
                   {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'},
                   {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}
                  ]
         }
compri = [n['name'] for n in tester['info']]
print(compri)

inner_list = tester['info']
import json
#print(json.dumps(inner_list, indent = 2))
compri = [d['name'] for d in inner_list]
print(compri)


lst = ['plum', 'watermelon', 'kiwi', 'strawberry', 'blueberry', 'peach', 'apple', 'mango', 'papaya']
print(lst)
#map filter
print(list(map(lambda x:x, filter(lambda x: len(x)>5 , lst))))
#listcomp
long_len = [st for st in lst if len(st)>5 ]
print(long_len)
