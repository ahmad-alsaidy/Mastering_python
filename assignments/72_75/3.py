nums = [2, 4, 6, 2]

# Output
# 96

from functools import reduce

def sum_of_nums(num1, num2):
    return num1 * num2

print(reduce(sum_of_nums, nums))
print(reduce((lambda num1, num2: num1 * num2), nums))
