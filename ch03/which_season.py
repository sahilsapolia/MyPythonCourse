print('Welcome to which session program')

month_string = input("Input the month number (e.g. January==1): ")
day_string = input("Input the day of the month (e.g. 19): ")

month = int(month_string)
day = int(day_string)

if month == 1 or month == 2 or month == 3:
    season = 'winter'
elif month == 4 or month == 5 or month == 6:
    season = 'spring'
elif month == 7 or month == 8 or month == 9:
    season = 'summer'
else:
    season = 'autumn'

if (month == 3) and (day > 19):
    season = 'spring'
elif (month == 6) and (day > 20):
    season = 'summer'
elif (month == 9) and (day > 21):
    season = 'autumn'
elif (month == 12) and (day > 20):
    season = 'winter'
print("Season is", season)

favourite_month = int(input("What is your favourite month? (e.g. January==1): "))

if favourite_month == 1 or favourite_month == 2 or favourite_month == 3:
    season = 'winter'
elif favourite_month == 4 or favourite_month == 5 or favourite_month == 6:
    season = 'spring'
elif favourite_month == 7 or favourite_month == 8 or favourite_month == 9:
    season = 'summer'
else:
    season = 'autumn' 

print("Favourite season is", season)
