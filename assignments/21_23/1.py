friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Osama" => Method One
# "Osama" => Method Two
# "Mahmoud" => Method One
# "Mahmoud" => Method Two

print(friends[0])  # Method one
print(friends.pop(0))  # Method two

print(friends[-1])  # Method one
print(friends.pop(-1))  # Method two
