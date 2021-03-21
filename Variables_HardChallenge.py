
# Print me IFF you can:
#   Write a program that reads two integers A,B
#     B is either -1 or 1:
#       if B is -1, print 2*A+1
#       if B is  1, print A**2
#   Input:  7 -1 => 49.0
#   Input:  7  1 => 15.0
    
# HINT:
#   Think of a one line formula for the output!

#USE of any branching statement(if, elif, else ...) is PROHIBITED!!





























































#################::ANSWER::#######################

....#BASICALLY think it as a kind of a MULTIPLEXER....
# Either 1*something + 0*something for b = 1
# Or     0*something + 1*something for b = -1

a, b = map(int, input().split())


# Let's code the 2 possible results
equ_is_1 = a * a
equ_is_neg_1 = 2 * a + 1

# The trick: we want to make them in 1 equation
# Where if input is: only 1 equation is computed and the second is zero
# To do so: convert -1 to 0 and 1 to 1
# With simple math, we can convert [-1 1] to [0 1] range

# value 1 for (b 1) and value 0 for (b -1)
is_1 = (b + 1) / 2
# value 1 for (b -1) and value 0 for (b 1)
is_neg_1 = 1 - is_1

# Either 1*something + 0*something for b = 1
# Or     0*something + 1*something for b = -1
ans = is_1 * equ_is_1 + is_neg_1 * equ_is_neg_1

print(ans)


######
# This is actually a trivial task as following:

if b == -1:
    print(2 * a + 1)
else:
    print(a * a)
