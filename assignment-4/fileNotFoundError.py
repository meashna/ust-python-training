# 3. Handle FileNotFoundError while opening a file
try:
    file = open("non_existing_file.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("3. Error: File not found")
