# ---------------------------
# -- Practical Slice Email --
# ---------------------------

name = input("What is your name? ").strip().capitalize()
email = input("What is your email? ").strip()

username = email[:email.index("@")]
domain = email[email.index("@") + 1:]

print("=" * 50)

print(f"Hello, {name}")
print(f"your username is: {username}\nYour Domain is: {domain}")

print("=" * 50)

