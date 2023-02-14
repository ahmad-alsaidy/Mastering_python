# Assignment 1 => done

import os

# os.mkdir(r"c:\Users\alsai\Desktop\Python")

os.chdir(r"c:\Users\alsai\Desktop\Python")

# file = open("assign.py", "w")

# for i in range(1, 51):
#     if i == 25:
#         file = open(f"Special-text.txt", "w")

#     else:
#         file = open(f"text{i}.txt", "w")

#     file.write(f"Elzero Web Scool => {i}")

# print(os.getcwd())

# print(os.path.abspath(__file__))

# print(os.path.basename(__file__))

# print(len(os.listdir(r"c:\Users\alsai\Desktop\Python")))

# --------------------------------------
# Assignment 2 => done

# file = open("text1.txt", 'a')

# file.write("\nAppend => Elzero Web School" * 50)

# --------------------------------------
# Assignment 3

infile = open("text1.txt", 'r')

lines = 0
words = 0
chars = 0
charL = 0

for line in infile.readlines():
    wordList = line.split()

    lines += 1

    words += len(wordList)

    # chars += sum(len(word) for word in wordList)

    chars += len(line.strip(os.linesep))  # after removing the linespace (\r\n)

    # charL += len(line)
    
    charL += line.count("l")

print(f"Number of Lines    => {lines}")
print(f"Number of Words    => {words}")
print(f"Number of Chars    => {chars}")
print(f"Number of Char 'l' => {charL}")

# --------------------------------------
# Assignment 4 => done

i = 50

# while i > 40:
#     os.remove(f"text{i}.txt")

#     i -= 1
