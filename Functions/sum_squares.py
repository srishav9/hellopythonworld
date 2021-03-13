def square(x):
    y=x*x
    return y
def sum_of_squares(x,y,z):
    a=square(x)
    c=square(y)
    b=square(z)
    return a+b+c

print("sum of squares of 10,11,12:",sum_of_squares(10,11,12))
