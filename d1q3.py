month = input("Enter the month: ")
date = int(input("Enter the date: "))
if (month == 'Mar' and date >= 20) or month == 'Apr' or month == 'May' or (month == 'Jun' and date < 21):
    season = 'Spring'
elif (month == 'Jun' and date >= 21) or month == 'Jul' or month == 'Aug' or (month == 'Sep' and date < 22):
    season = 'Summer'
elif (month == 'Sep' and date >= 22) or month == 'Oct' or month == 'Nov' or (month == 'Dec' and date < 21):
    season = 'Fall'
else:
    season = 'Winter'
print("The season is currently", season)
