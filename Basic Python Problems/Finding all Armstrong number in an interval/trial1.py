lowerLimit, upperLimit = input(
    "Enter the lower and upper limit : ").strip().split()

armstrongList = []
for num in range(int(lowerLimit), (int(upperLimit)+1)):
    sum = 0
    for digit in str(num):
        sum += int(digit) ** 3
    if sum == num:
        armstrongList.append(num)
print(armstrongList)
