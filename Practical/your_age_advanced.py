# -------------------------------------------------
# -- Calculate Age Advanced Version and Training --
# -------------------------------------------------

print('=' * 60)
print(" Advanced Age Calculator ".center(60, '='))
print('=' * 60)

# Getting The Age In Years From The User
age = int(input("Add your age in years: ").strip())
print('=' * 60)

# Getting The New Unit From The User
unit = input("Choos one of these units: [m => month] [w => week] [d => day] [h => hour] [n => minute] [s => second]\n").strip().lower()
print('=' * 60)

# Units of Time
months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

# Printing Age In The New Unit
if unit == 'm' or unit == 'month':
    print("You choosed month.")
    print(f"Your age in months is: {months:,}")
elif unit == 'w' or unit == 'week':
    print("You choosed week.")
    print(f"Your age in weeks is: {weeks:,}")
elif unit == 'd' or unit == 'day':
    print("You choosed day.")
    print(f"Your age in days is: {days:,}")
elif unit == 'h' or unit == 'hour':
    print("You choosed hour.")
    print(f"Your age in hours is: {hours:,}")
elif unit == 'n' or unit == 'minute':
    print("You choosed minute")
    print(f"Your age in minutes is: {minutes:,}")
else:
    print("You choosed Second.")
    print(f"Your age in seconds is: {seconds:,}")

print('=' * 60)