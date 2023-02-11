tries = 4

mainPassword = 'Ahmad@123'

tries = 4

while tries > 0:
    inputPassword = input(">> Add Your Password: ").strip()

    if inputPassword != mainPassword:
        tries -= 1

        if tries == 0:
            print("You Have Finished Your Tries.")

            break

        print(f"You Have {tries} Tries Left.")

    else:
        print("Correct Password. Welcom.")

        break
