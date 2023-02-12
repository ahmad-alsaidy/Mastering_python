# Needed Output
# "01"
# "02"
# "03"
# "04"
# "05"
# "07"
# "09"
# "10"
# "11"
# "13"
# "14"
# "15"
# "16"
# "17"
# "18"
# "19"
# "20"
# "All Numbers Printed"

for i in range(1, 21):
    if i == 6 or i == 8 or i == 12:
        continue

    print(str(i).zfill(2))

else:
    print("All numbers printed.")