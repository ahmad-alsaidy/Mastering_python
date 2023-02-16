my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
    # Write Your Code Here
    if type(item2) == int:
        my_data.append(item1.lower())
    else:
        if type(item1) == int:
            break
        if item1 == "E":
            my_data.append(item1)
        else:
            my_data.append(item1.lower())


final_string = "".join(my_data)

print(final_string)  # Elzero
