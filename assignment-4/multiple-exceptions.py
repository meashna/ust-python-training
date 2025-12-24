# Handle multiple exceptions in a single try block
try:
    num = int("abc")
    res = 10 / 0
except ValueError:
    print("5. ValueError occurred")
except ZeroDivisionError:
    print("5. ZeroDivisionError occurred")
