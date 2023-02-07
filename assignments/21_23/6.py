friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

# Needed Output
# ["Ahmed", "Sayed", "Salem"]
# ["Ahmed", "Sayed"]

friends[0:2] = []
print(friends)

friends.remove("Salem")
print(friends)