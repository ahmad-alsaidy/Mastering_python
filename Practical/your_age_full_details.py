# -------------------------------------
# -- Practical Your Age Full Details --
# -------------------------------------

# Take input from the user
ageYears = int(input('What\'s your age in years: ').strip())

# Convert age in years to all time units
ageMonths = ageYears * 12
ageWeeks = ageMonths * 4
ageDays = ageYears * 365
ageHours = ageDays * 24
ageMinutes = ageHours * 60
ageSeconds = ageMinutes * 60

# Print data
print('=' * 50)
print('You Lived For: ')
print(f"{ageMonths:,} Months.")
print(f"{ageWeeks:,} Weeks.")
print(f"{ageDays:,} Days.")
print(f"{ageHours:,} Hours.")
print(f"{ageMinutes:,} Minutes.")
print(f"{ageSeconds:,} Seconds.")
