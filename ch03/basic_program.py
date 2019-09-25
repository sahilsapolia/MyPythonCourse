keep_looping = True

while keep_looping:
    month = int(input("Enter a month numnerically: "))
    if (month > 0 and month < 13):
        day = int(input("Enter a day numerically: "))
        if (day > 0 and day <= 31):
            keep_looping = False
    else:
        print('Invalid entries. Enter 1-12 for month, enter 1-31 for days')
