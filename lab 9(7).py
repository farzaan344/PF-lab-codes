print("Farzaan Bin Khawar\n2023F-BIT-030")
import random

def merge_sorted_lists(list1, list2):
    merged_list = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])

    return merged_list

list1 = sorted(random.sample(range(1, 101), 10))
list2 = sorted(random.sample(range(1, 101), 8))

print("List 1:", list1)
print("List 2:", list2)

merged_result = merge_sorted_lists(list1, list2)

print("\nMerged List:", merged_result)
