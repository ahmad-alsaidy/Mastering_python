my_set = {1, 2, 3}
letters = {"A", "B", "C"}

# Needed Output

# {1, 2, 3}
# set()
# {"A", "B"}

print(my_set)

my_set.clear()
print(my_set)

my_set.update("A", "B") # Method 1 to add 'A' and 'B'

# Method 2 to add 'A' and 'B'
letters.remove("C")
my_set.update(letters)

print(my_set)

my_set.discard("C")