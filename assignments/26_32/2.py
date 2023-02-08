nums = {1, 2, 3}
letters = {"A", "B", "C"}

# Needed Output

# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}

print(nums | letters) # Method 1
print(nums.union(letters)) # Method 1

print(nums.symmetric_difference(letters)) # Method 2

nums.update(letters) # Method 3
print(nums)