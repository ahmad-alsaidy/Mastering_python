# The Date Is "2021, 6, 25"
# Today Is "2021, 8, 10"

# Message Will Be
# "Days From 2021-06-25 To 2021-08-10 Is => 46"
import datetime

someDate = datetime.datetime(2021, 6, 25)
today = datetime.datetime(2021, 8, 10)

days = (today - someDate).days

someDate = someDate.strftime("%Y-%m-%d")
today = today.strftime("%Y-%m-%d")

print(f"Days From {someDate} To {today} Is => {days}")