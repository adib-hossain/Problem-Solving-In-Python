a = 2
prime_number = True

if a == 1:
    print("Not a Prime Number")
else:
    for i in range(2, a):
        if (a % i) == 0:
            print("Not a Prime Number")
            prime_number = False
            break
    if prime_number:
        print("Prime Number")

#  listing prime numbers .Not origanally wanted but added out of curiosity


Prime_list = []

for num in range(1, 101):
    prime_number = True

    for i in range(2, num):
        if (num % i) == 0:
            prime_number = False
            break
    if prime_number:
        Prime_list.append(num)

print(Prime_list)
