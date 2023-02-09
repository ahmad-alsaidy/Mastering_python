# Inputs:

# "Osama@Nn.Sa" # Email

# Needed Output:

# "Your Name Is Osama"
# "Email Service Provider Is nn"
# "Top Level Domain Is sa"

email = input("Your Email: ").strip().lower()

print("Your name is: {}".format(email[:email.index("@")]))
print("Email Service Provider is: {}".format(email[email.index("@") + 1:email.index(".")]))
print("Top Level Domain is: {}".format(email[email.index(".") + 1:]))