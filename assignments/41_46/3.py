# Input Example 38

# Needed Output
# "Your Age In Months Is 456 Months" # Months Example
# "Your Age In Weeks Is 1824 Weeks" # Weeks Example

age = int(input("Add Your Age: ").strip())

if age > 10 and age < 100:
    print(f"Your Age In Months: {age * 12:,} Months.")
    print(f"Your Age In Weeks: {age * 12 * 4:,} Weeks.")
    print(f"Your Age In Days: {age * 365:,} Days.")
    print(f"Your Age In Hours: {age * 365 * 24:,} Hours.")
    print(f"Your Age In Minutes: {age * 365 * 24 * 60:,} Minutes.")
    print(f"Your Age In Seocnds: {age * 365 * 24 * 60:,} Seocnds.")

else:
    print("Your Age Is Out of Range!")