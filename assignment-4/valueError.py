# 2. Handle ValueError when input is not an integer
try:
    num = int("abc")   # invalid integer
    print("Number:", num)
except ValueError:
    print("2. Error: Input is not an integer")
