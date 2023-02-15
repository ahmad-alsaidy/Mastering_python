# Today Is "2021, 8, 10"

# "2021-08-10"
# "Aug 10, 2021"
# "10 - Aug - 2021"
# "10 / Aug / 21"
# "10 / August / 2021"
# "Tue, 10 August 2021"
import datetime

today = datetime.datetime(2021, 8, 10)

print(today.strftime("%Y-%m-%d"))  # "2021-08-10"
print(today.strftime("%b %d, %Y"))  # "Aug 10, 2021"
print(today.strftime("%d - %b - %Y"))  # "10 - Aug - 2021"
print(today.strftime("%d / %b / %y"))  # "10 / Aug / 21"
print(today.strftime("%d / %B / %Y"))  # "10 / August / 2021"
print(today.strftime("%a, %d %B %Y"))  # "Tue, 10 August 2021"
