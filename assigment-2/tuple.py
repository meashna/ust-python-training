# 1. Can you modify the elements of a tuple after it has been created?
# No, tuples are immutable, so elements cannot be changed after creation.
t = (1, 2, 3, 4)
print("1. Tuple is immutable, original tuple:", t)


# 2. Access the second-to-last element in a tuple
t2 = (10, 20, 30, 40, 50)
print("2. Second-to-last element:", t2[-2])


# 3. Difference between a list and a tuple
# List is mutable, tuple is immutable
lst = [1, 2, 3]
tpl = (1, 2, 3)
print("3. List:", lst, "| Tuple:", tpl)


# 4. Change the value 3 to 100 in the tuple t = (1, 2, 3, 4)
t3 = (1, 2, 3, 4)
t3 = t3[:2] + (100,) + t3[3:]
print("4. Tuple after changing value:", t3)


# 5. Function that returns the sum of all elements in a tuple
def tuple_sum(t):
    return sum(t)


print("5. Sum of tuple elements:", tuple_sum((1, 2, 3, 4, 5)))
