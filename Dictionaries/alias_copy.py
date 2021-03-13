
#ALIAS
opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'}
alias = opposites
print(opposites)
print("alias = opposites")
print("The 'is' operator shows if two objects are same")
print("alias is opposites",alias is opposites)
alias['right'] = 'left'
print("alias['right'] = 'left'")
print("opposites['right']:",opposites['right'])

#COPY
acopy=opposites.copy()
print("acopy=opposites.copy()")
print("acopy['right'] = 'wrong'")
acopy['right'] = 'wrong'
print(opposites,"Original object is not changed")
