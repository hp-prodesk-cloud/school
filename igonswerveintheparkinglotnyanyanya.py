day = input('enter a day of the month in a number')
day = int(day)
month = input('enter a month of the year in number')
month = int(month)
year = input('enter the last 2 digits of a year')
year = int(year)
m1 = day * month
if m1 == year: 
    print('your year is special')
else :
    print('your year is not special')