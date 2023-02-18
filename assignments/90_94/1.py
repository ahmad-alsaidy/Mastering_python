NUM = input("Add Your Number ")

# Your Code Here
if len(NUM) > 1:
    raise IndexError("Only One Character Allowed")
elif NUM.isalpha():
    raise Exception("Only Numbers Allowed")
elif int(NUM) <= 0:
    raise ValueError("Number Must Be Larger Than 0")