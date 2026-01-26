# Using loop

a = 5


if a <= 0:
    print(0)
else:
    for i in range(1, a):
        a *= i
    print(a)
