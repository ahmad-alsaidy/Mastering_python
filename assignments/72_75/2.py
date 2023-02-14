friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

# Output
# "Wessam"
# "Essam"

def get_names(str):
    return str.endswith('m')

names = filter(get_names, friends_filter)

for name in names:
    print(name)

print('=' * 30)

for name in filter((lambda str: str.endswith('m')), friends_filter):
    print(name)