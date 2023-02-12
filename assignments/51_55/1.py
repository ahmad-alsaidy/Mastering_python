# Input
my_nums = [15, 81, 5, 17, 20, 21, 13]

# Needed Output
# "1 => 20"
# "2 => 15"
# "3 => 5"
# "All Numbers Printed"

counter = 0
my_nums.sort(reverse=True)

for i in my_nums:
    if i % 5 == 0:
        counter += 1

        print(f"{counter}) {i}")
