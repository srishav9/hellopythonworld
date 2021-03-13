def square(x):
    y = x * x
    return y

toSquare = 10
result = square(toSquare)
print("The result of {} squared is {}.".format(toSquare, result))

def square(x):
    y = x * x
    print(y)   # Bad! This is confusing! Should use return instead!
toSquare = 10
squareResult = square(toSquare)
print("The result of {} squared is {}.".format(toSquare, squareResult))



def square(x):
    y = x * x
    return y   # Bad! This is confusing! Should use return instead!
toSquare = 10
squareResult = square(toSquare)
print("The result of {} squared is {}.".format(toSquare, squareResult))
