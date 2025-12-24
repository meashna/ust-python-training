# 4. Use try, except, else, and finally blocks
try:
    x = int("5")
    y = 2
    result = x / y
except Exception:
    print("4. Error occurred")
else:
    print("4. Division successful:", result)
finally:
    print("4. Execution completed")
