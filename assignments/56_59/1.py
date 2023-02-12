def calculate(num1, num2, operator='add'):
    operator = operator.strip().lower()

    if operator == 'add' or operator == 'a':
        return (num1 + num2)

    elif operator == 'subtract' or operator == 's':
        return (num1 - num2)

    elif operator == 'multiply' or operator == 'm':
        return (num1 * num2)

    else:
        return ("This operation is not available.")

# Test
print(calculate(10, 20)) # 30
print(calculate(10, 20, "AdD")) # 30
print(calculate(10, 20, "a")) # 30
print(calculate(10, 20, "A")) # 30

print(calculate(10, 20, "S")) # -10
print(calculate(10, 20, "subTRACT")) # -10

print(calculate(10, 20, "Multiply")) # 200
print(calculate(10, 20, "m")) # 200