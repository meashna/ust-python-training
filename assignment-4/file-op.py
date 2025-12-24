# 1. Create a text file and write multiple lines into it
file = open("data.txt", "w")
file.write("Python is easy\n")
file.write("File handling in Python\n")
file.write("This is a text file example\n")
file.close()
print("1. File created and written successfully")


# 2. Read the contents of a text file line by line
file = open("data.txt", "r")
print("2. Reading file line by line:")
for line in file:
    print(line.strip())
file.close()


# 3. Count the number of lines, words, and characters in a text file
file = open("data.txt", "r")
lines = file.readlines()
file.close()

line_count = len(lines)
word_count = sum(len(line.split()) for line in lines)
char_count = sum(len(line) for line in lines)

print("3. Number of lines:", line_count)
print("3. Number of words:", word_count)
print("3. Number of characters:", char_count)


# 4. Copy the contents of one text file into another file
source_file = open("data.txt", "r")
destination_file = open("data_copy.txt", "w")
destination_file.write(source_file.read())
source_file.close()
destination_file.close()
print("4. File copied successfully")


# 5. Search for a specific word in a text file and display line numbers
search_word = "Python"
file = open("data.txt", "r")

print("5. Searching for word:", search_word)
for line_number, line in enumerate(file, start=1):
    if search_word in line:
        print("Found at line number:", line_number)

file.close()
