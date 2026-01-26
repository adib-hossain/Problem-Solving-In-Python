a = 2100

if (a % 100) == 0 and (a % 400) == 0:
    print("Leap Year")
elif (a % 4) == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")
