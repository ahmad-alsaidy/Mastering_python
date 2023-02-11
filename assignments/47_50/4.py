# Input
# name = "OSAMA"

# Needed Output
# "Invalid Name"
# ----------------------
# Input
# name = "osama"

# Needed Output
# "Friend osama Added => 1st Letter Become Capital"
# "Names Left in List Is 3"
# ----------------------
# Input
# name = "Ahmed"

# Needed Output
# "Friend Ahmed Added"
# "Names Left in List Is 2"
# ----------------------

my_friends = []

max_friends_num = 4


while max_friends_num > 0:
    friend_name = input("Add The Friend Name: ").strip()

    while friend_name.isupper():
        print("Invalide Friend Name.")
        
        friend_name = input("Add The Friend Name: ").strip()

    if friend_name[0].islower():
        friend_name = friend_name.capitalize()

        my_friends.append(friend_name)

        print(f"Friend {friend_name} Added => 1st Letter Become Capital")

    else:
        friend_name = friend_name.capitalize()

        my_friends.append(friend_name)

        print(f"Friend {friend_name} Added")

    max_friends_num -= 1

    print(f"Names Left in The List Is {max_friends_num}")

else:
    print(my_friends)
