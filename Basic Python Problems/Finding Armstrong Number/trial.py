num = input("Enter Num : ").strip()
sum = 0

for digit in num:
    sum += int(digit)**3
if int(num) == sum:
    print("This is an Armstrong Number")
else:
    print("Not an Armstrong Number")
