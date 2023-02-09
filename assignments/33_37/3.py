num_one = 10
num_two = 20
num = 20

# Needed Output
# True
# False

print(bool((num > num_one and not num > num_two) or (num > num_two and not num > num_one)))

print(bool(num > num_one and num > num_two))