print("Farzaan Bin Khawar\n2023F-BIT-030")
def linear_search(lst, element):
    for value in lst:
        if value == element:
            return lst.index(value)
    return 'not found'

my_list = [2, 5, 8, 12, 16, 23, 38, 42]
search_element = 16

result = linear_search(my_list, search_element)

if result != 'not found':
    print('The element', search_element, 'is found at position', result, '.')
else:
    print('The element', search_element, 'is not found in the list.')
