print("Farzaan Bin Khawar\n2023F-BIT-030")
num = int(input("Enter an integer: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    factorial = 1

    i = 1
    while i <= num:
        factorial *= i
        i += 1

    print(f"The factorial of {num} is {factorial}")