# Input
# num = 0

# Needed Output
# "Number 0 Is Not Larger Than 0"
# -----------------------------------
# Input
# num = 10

# Needed Output
# 9
# 8
# 7
# 5
# 4
# 3
# 2
# 1
# "8 Numbers Printed Successfully."
# -----------------------------------

num = int(input("add number: ").strip())

printedNum = 0

if num > 0:
    while num > 1:
        num -= 1

        if num == 6:
            num -= 1

        print(num)

        printedNum += 1

    print(f"{printedNum} Numbers Pirnted Successfully.")

else:
    print("Number 0 Is Not Larger Than 0")