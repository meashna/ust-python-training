# 1. How does the map() function work?
# map() applies a function to each element in a list
from math import gcd
from functools import reduce
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, numbers))
print("1. Squares using map():", squares)


# 2. Output of the given reduce() code

result = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print("2. Output of reduce():", result)
# Output: 24


# 3. Convert all string elements of a list to uppercase using map()
words = ["python", "map", "reduce"]
uppercase_words = list(map(str.upper, words))
print("3. Uppercase words:", uppercase_words)


# 4. Find the GCD of a list of numbers using reduce()

numbers_list = [12, 24, 36]
gcd_result = reduce(gcd, numbers_list)
print("4. GCD of the list:", gcd_result)


# 5. Compare map() and filter()
# map() transforms elements
# filter() selects elements based on a condition
nums = [1, 2, 3, 4, 5]
mapped = list(map(lambda x: x * 2, nums))
filtered = list(filter(lambda x: x % 2 == 0, nums))
print("5. map() result:", mapped)
print("5. filter() result:", filtered)
