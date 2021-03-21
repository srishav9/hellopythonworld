stri = input()           # enter hello world
print(stri)              # hello world
print(type(stri))        # <class 'str'>

stri = input()           # enter 12
print(stri, type(stri))   # 12 <class 'str'>

# read 3 strings
a, b, c = input().split()

#Let’s read 4 integers:
a, b, c, d = map(int, input().split())

#Let’s read 5 floats
a, b, c, d, e = map(float, input('Enter 5 numbers: ').split())

first = input('Enter first number: ')
first = float(first)

# let's make it in a single line
second = float(input('Enter second number: '))

#INTERESTING FACTS:

n = int(input())
ans = (n * (n + 1)) / 2
"""
Why such equation?
Here is an intuition for N = 8
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
Let's arrange as following
1 8   2 7    3 6     4 5       [first number and last number]   [2nd number, and 2nd from back] ...
What is the value of each pair? 9 = n+1
How many pairs? 4 = n/2
So n/2 pair, each has value n+1
So total sum is (n * (n+1))/2

Now, this works for even N
Your turn: why works for odd N
More readings: http://mathcentral.uregina.ca/qq/database/qq.02.06/jo1.html
"""
