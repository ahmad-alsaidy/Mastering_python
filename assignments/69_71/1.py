values = (0, 1, 2)

if any(values):  # if any value is ture => make a variable 'my_var = 0'

    my_var = 0  # there is a two value are true => so the variable will be made

my_list = [True, 1,  1, ["A", "B"], 10.5, my_var] # my_var = 0 = False

if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

    print("Good")

else:

    print("Bad")

# Output : Good => Because: all(my_list[:4]) = True
