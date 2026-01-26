a = 2100


def yes():
    print("Leap Year")


def no():
    print("Not a Leap Year")


if (a % 100) == 0:
    if (a % 400) == 0:
        yes()
    else:
        no()
elif (a % 4) == 0:
    yes()
else:
    no()
