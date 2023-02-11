# ----------------------------
# -- Loop => While Training --
# -- Simple Bookmark Manage --
# ----------------------------

# Empty List To Fill
myBookmarks = []

# Maximum Allowed Number of Bookmarks
maximumBookmarks = 5

# Filling The Bookmark List
while maximumBookmarks > 0:
    website = input("Add A Website Without https:// ").strip().lower()

    myBookmarks.append(f"https://{website}")

    maximumBookmarks -= 1

    print(f"Website Added. {maximumBookmarks} Places Left.")

    print(myBookmarks)
else:
    print('=' * 40)
    print("Bookmark List Is Full. No Other Places Available.")
    print('=' * 40)

# Check If The List Is Not Empty => Print Bookmarks
if len(myBookmarks) > 0:
    # Sort The List
    myBookmarks.sort()

    index = 0

    while index < len(myBookmarks):
        print(myBookmarks[index])

        print('-' * 40)
        
        index += 1
