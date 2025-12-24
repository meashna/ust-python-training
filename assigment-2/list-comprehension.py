# 1. List comprehension that returns all even numbers from 0 to 20
even_numbers = [i for i in range(21) if i % 2 == 0]
print("1. Even numbers from 0 to 20:", even_numbers)


# 2. Create a new list of squares from an existing list using list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [i * i for i in numbers]
print("2. Squares of numbers:", squares)


# 3. Extract all words longer than 4 characters from a sentence
sentence = "List comprehension in Python is very powerful"
long_words = [word for word in sentence.split() if len(word) > 4]
print("3. Words longer than 4 characters:", long_words)


# 4. Generate a list of the first 10 Fibonacci numbers using list comprehension
fib = [0, 1]
[fib.append(fib[-1] + fib[-2]) for _ in range(8)]
print("4. First 10 Fibonacci numbers:", fib)


# 5. Use if condition inside list comprehension to select only odd numbers
nums = [1, 2, 3, 4, 5, 6, 7]
odd_numbers = [i for i in nums if i % 2 != 0]
print("5. Odd numbers from the list:", odd_numbers)
