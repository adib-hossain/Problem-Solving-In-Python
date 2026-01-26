# Using Recursion
def fact(x):
    if x >= 2:
        return (x * fact(x-1))
    else:
        return 1


print(fact(4))
