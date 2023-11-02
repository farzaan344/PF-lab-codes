print("Farzaan Bin Khawar\n2023F-BIT-030")
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

if num1 < num2:
    lowest = num1
    highest = num2
else:
    lowest = num2
    highest = num1
print(f"Highest value: ",highest)
print(f"Lowest value: ",lowest)