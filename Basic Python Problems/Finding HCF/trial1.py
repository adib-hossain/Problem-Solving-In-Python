def findHCF(x, y):
    bigger_num, smaller_num = 0, 0

    if x > y:
        bigger_num = x
        smaller_num = y
    else:
        bigger_num = y
        smaller_num = x

    while True:
        if bigger_num % smaller_num == 0:
            return smaller_num
        else:
            smaller_num = bigger_num % smaller_num
            bigger_num = smaller_num
            if smaller_num == 0:
                return 1


print("The HCF is : ",findHCF(10, 40))
