listNum = [10, 45, 64, 35, 78, 95, 16, 345, 54, 78, 14, 954, 426, 478, 635]
dividend = 15

resulstList = []

for item in listNum:
    if item % dividend == 0:
        resulstList.append(item)

print(dividend)
print(resulstList)
