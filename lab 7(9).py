print("Farzaan Bin Khawar\n2023F-BIT-030")
def GCD(a, b):
    while b:
        a, b = b, a % b
    return a
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = GCD(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")