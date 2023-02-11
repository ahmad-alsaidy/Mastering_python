# Input
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]

# Needed Output
# "Mohamed"
# "Shady"
# "Sherif"
# "Friends Printed And Ignored Names Count Is 2"

a = 0

lowerNames = 0

while a < len(friends):
    if friends[a][0].islower():
        lowerNames += 1
    
    elif friends[a][0].isupper():
        print(friends[a])
    
    a += 1

print(f"Friends Printed And Ignored Names Count Is {lowerNames}")