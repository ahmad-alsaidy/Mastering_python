friends = ("Osama", "Ahmed", "Sayed")

# Needed Output

# ("Elzero", "Ahmed", "Sayed")
# <class 'tuple'>
# 3 Elements

friends = ("Elzero", ) + friends[1:]
print(friends)
print(type(friends))
print(len(friends))