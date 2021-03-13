def hello():
    """Inside these triple quotes are called docstrings
    Used for functions and are not completely eliminated when the program is parsed
    way to retrieve this information is to use the interactive interpreter, and enter the expression <function_name>.__doc__,
    which will retrieve the docstring for the function.
    So the string you write as documentation at the start of a function is retrievable by python tools at runtime.
    {ENTER q to QUIT}

    Says Hello"""
    print("Hello")
    print("Glad we are here")

hello()
#print("FROM DOC is NEXT")
#print(hello.__doc__)
#help(hello)
