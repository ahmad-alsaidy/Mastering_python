# Inputs

# "Osama" # First Name
# "Mohamed" # Second Name

# Needed Output

# "Hello {First_Name} {First_Letter_From_Second_Name}." # Example "Osama M."

first_name = input("Frist name:").strip().capitalize()
Second_name = input("Second name:").strip().capitalize()

print(f"Hello {first_name} {Second_name:.1s}.")