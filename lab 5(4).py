print("Farzaan Bin Khawar\n2023F-BIT-030")
table_number = int(input("Enter the table number: "))
table_limit = int(input("Enter the table limit: "))

if table_number <= 0 or table_limit <= 0:
    print("Both values must be positive integers.")
else:
    print(f"Table for {table_number} up to {table_limit}:")
    for i in range(1, table_limit + 1):
        result = table_number * i
        print(f"{table_number} x {i} = {result}")