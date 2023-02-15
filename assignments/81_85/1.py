def reverse_string(my_string):
    # Your Code Here
    yield my_string[::-1]

    # Reverse The String
for c in reverse_string("Elzero"):
    print(c)
