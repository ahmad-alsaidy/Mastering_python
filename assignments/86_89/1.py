my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

for data in zip(my_list, my_tuple):
    # Write Your Code Here
    if data[0] == "E":
        my_data.append(data[0])
        my_data.append(data[1].lower())

    else:
        my_data.append(data[0].lower())
        my_data.append(data[1].lower())

final_string = "".join(my_data)

print(final_string)  # Elzero
