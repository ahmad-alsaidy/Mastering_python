friends = ["Osama", "Ahmed", "Sayed"]

# Needed Output
# ["Nasser", "Osama", "Ahmed", "Sayed"]
# ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

friends.insert(0, "Nasser")
print(friends)

friends.append("Salem")
print(friends)