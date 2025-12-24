# 1. Add an element at the end of a list
lst = [1, 2, 3, 4, 5]
lst.append(6)
print("1. After adding element at the end:", lst)


# 2. Remove an element from a list by its index
lst2 = [10, 20, 30, 40, 50]
del lst2[2]
print("2. After removing element at index 2:", lst2)


# 3. Output of the given code snippet
lst3 = [1, 2, 3, 4, 5]
lst3[1:3] = [10, 20]
print("3. Output of slice assignment:", lst3)
# Output: [1, 10, 20, 4, 5]


# 4. Check if an element exists in a list
lst4 = [5, 10, 15, 20]
if 10 in lst4:
    print("4. Element exists in the list")
else:
    print("4. Element does not exist in the list")


# 5. Remove duplicates from a list without using set()
def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


lst5 = [1, 2, 2, 3, 4, 4, 5]
print("5. List after removing duplicates:", remove_duplicates(lst5))
