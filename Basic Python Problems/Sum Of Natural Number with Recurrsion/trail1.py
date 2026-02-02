def sumWithRec(n):
    if n <= 1:
        return n
    else:
        return n + sumWithRec(n-1)


print(sumWithRec(10))
