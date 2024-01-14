print("Farzaan Bin Khawar\n2023F-BIT-030")
def common_member(list1, list2):
    for element in list1:
        if element in list2:
            return True
    return False

data_set1 = [1, 2, 3, 4, 5]
data_set2 = [5, 6, 7, 8, 9]

Firstresult = common_member(data_set1, data_set2)
print("Data Set 1:", data_set1)
print("Data Set 2:", data_set2)
print("Do they have a common member?", Firstresult)

data_set3 = ["apple", "banana", "orange"]
data_set4 = ["grape", "kiwi", "orange"]

Secondresult = common_member(data_set3, data_set4)
print("\nData Set 3:", data_set3)
print("Data Set 4:", data_set4)
print("Do they have a common member?", Secondresult)
