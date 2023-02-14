friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

# Output
# "Eman"
# "Ahmed"
# "Sameh"
# "Osama"

def remove_chars(str):

    return str[1:-1]

cleaned_list = map(remove_chars, friends_map)

for s in cleaned_list:
    print(s)

print('=' * 30)

for s in map((lambda str: str[1:-1]), friends_map):
    print(s)