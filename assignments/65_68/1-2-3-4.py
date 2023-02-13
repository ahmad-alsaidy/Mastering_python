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

# file.write("\nAppend => Ezero Web School" * 50)

# --------------------------------------
# Assignment 3

file = open("text1.txt", 'r')
# count lines
# count words
# count chars
# count char 'l'

# --------------------------------------
# Assignment 4 => done

i = 50

while i > 40:
    os.remove(f"text{i}.txt")

    i -= 1
