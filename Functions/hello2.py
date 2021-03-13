def hello2(s):
    """
    Function invocations always work that way.
    The expression inside the parentheses on the line that invokes the function
    is evaluated before control is passed to the function.
    The value is assigned to the corresponding formal parameter.
    Then, when the code block inside the function is executing,
    it can refer to that formal parameter and get its value,
    the value that was ‘passed into’ the function.
    """
    print("Hello " + s)
    print("Glad to meet you")
hello2("Nick")
hello2("Nicky")
hello2("Nickmo")
hello2("Iman" + " and Jackie")
hello2("Class " * 3)
print()
print()
def hello3(s, n):
    greeting = "Hello {} ".format(s)
    print(greeting*n)
hello3("Wei", 4)
hello3("", 1)
hello3("Kitty", 11)

#s,n        => FORMAL parameters
#"Wei",4    => ACTUAL parameters
#s="Wei" and n=4 is what happens behind.
