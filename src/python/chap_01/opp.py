from datetime import datetime
import time
import random

odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25
    , 27, 29, 31, 33, 35, 37, 41, 43, 45, 47, 49
    , 51, 53, 55, 57, 59]


for i in range(5):
    time_right_now = datetime.now()

    if time_right_now.minute in odd:
        print("That's an odd minute")
    else:
        print("Everything is even going here")

    time.sleep(random.randint(1, 60))

