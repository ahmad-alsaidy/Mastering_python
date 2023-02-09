num_one = 10
num_two = 20

# Needed Output
# 30
# 27000
# 1000
# 200.0
# <class 'str'>

result = num_one + num_two

print(result)  # 30
print(result ** 3)  # 27000
print((result ** 3) % 26000)  # 1000
print(((result ** 3) % 26000) / 5.0)  # 200.0
print(type(str(result)))  # <class 'str'>
