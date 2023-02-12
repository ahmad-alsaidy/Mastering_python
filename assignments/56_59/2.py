def addition(*numbers):
    sum = 0

    for num in numbers:
        if num == 10:
            continue

        if num == 5:
            sum -= 5
        else:
            sum += num

    return sum

# Tests
print(addition(10, 20, 30, 10, 15)) # 65
print(addition(10, 20, 30, 10, 15, 5, 100)) # 160