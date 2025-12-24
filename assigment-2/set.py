# 1. Remove all elements from a set
s = {1, 2, 3, 4}
s.clear()
print("6. Set after removing all elements:", s)


# 2. Output of the given code snippet
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("7. Output of a - b:", a - b)
# Output: {1, 2}


# 3. Check if an element is present in a set
s2 = {10, 20, 30}
if 20 in s2:
    print("8. Element is present in the set")
else:
    print("8. Element is not present in the set")


# 4. Program to find the intersection of two sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}
intersection = set1 & set2
print("9. Intersection of two sets:", intersection)


# 5. How does a set handle duplicate values?
# Sets automatically remove duplicate values
s3 = {1, 1, 2, 2, 3, 3}
print("10. Set after adding duplicates:", s3)
