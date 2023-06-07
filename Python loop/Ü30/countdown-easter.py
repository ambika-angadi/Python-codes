#import datetime class from datetime module
from datetime import datetime
import time

# set the easter date and time
easter_date = datetime(2023, 4, 11, 0, 0, 0) 

#set and output today's date in string format
today_date = datetime.now()
print("Today's date and time =", today_date.strftime("%d/%m/%Y %H:%M:%S"))
print("Easter date and time =", easter_date.strftime("%d/%m/%Y %H:%M:%S"))

# calculate the time difference
time_difference = easter_date - datetime.now() 

#loop until countdown is finished
while time_difference.days < 0:
    break
print(f"{time_difference.days} days, {time_difference.seconds//3600} hours, {time_difference.seconds%3600//60} minutes, {time_difference.seconds%60} seconds")
time.sleep(1) 






