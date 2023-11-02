print("Farzaan Bin Khawar\n2023F-BIT-030")
factorials = []

for _ in range(3):
    num = int(input("Enter an integer: "))
    
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    
    factorials.append(factorial)
    
for i in range(3):
    print(f"The factorial of {factorials[i]} is {factorials[i]}")