# ----------------------------------
# -- Practical Membership Control --
# ----------------------------------

print('=' * 50)
print(" Login ".center(50, '='))
print('=' * 50)

# List of Admins
admins = ["Ahmad", "Ali", "Osama", "Muhammad"]

# Login
name = input("Wha's Your Name? ").strip().capitalize()
print('=' * 50)

# If Name Is In Admins
if name in admins:
    print(f"Hello, {name}\nYou are an admin.")

    print('=' * 50)

    option = input("Update[U] or Delete[D]? ").strip().capitalize()

    # Update Option
    if option == 'Update' or option == 'U':
        newName = input("Add the new name: ").strip().capitalize()

        admins[admins.index(name)] = newName

        print('=' * 50)

        print("Name Updated.")

        print(admins)

        print('=' * 50)

    # Delete Option
    elif option == 'Delete' or option == 'D':
        admins.remove(name)

        print('=' * 50)

        print("Name Deleted.")

        print(admins)

        print('=' * 50)
    # Wrong Prompt
    else:
        print("Wrong Prompt")

        print('=' * 50)

# If Name Is Not In Admins
else:
    status = input("You are not an admin. Add You? [Yes, No] ").strip().capitalize()
    print('=' * 50)

    if status == 'Yes' or status == 'Y':
        admins.append(name)

        print("Added To Admins.")

        print(admins)

        print('=' * 50)

    else:
        print("You Are Not Added.")

        print('=' * 50)
