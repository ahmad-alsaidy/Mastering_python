# Inputs

# num1 = 20
# num2 = 40
# operation = "+" Or "-" Or "*" Or "/" Or "%"

# Needed Output

# [num1 20] [operation +] [num2]
# Example One 20 + 40 = 60
# Example Two 20 * 40 = 800

num1 = int(input("Frist Number: ").strip())
num2 = int(input("Second Number: ").strip())

operation = input("Operation: [+][-][*][/][%] ").strip()

if operation == '+':
    print(num1 + num2)

elif operation == '-':
    print(num1 - num2)

elif operation == '*':
    print(num1 * num2)

elif operation == '/':
    print(num1 / float(num2))

elif operation == '%':
    print(num1 % num2)

else:
    print("You Entered Wrong Operation!")
