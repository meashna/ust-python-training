# 1. Handle ZeroDivisionError
try:
    a = 10
    b = 0
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("1. Error: Cannot divide by zero")
