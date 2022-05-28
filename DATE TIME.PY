#DATE TIME IN PYTHON
import datetime as dt    #I AM GIVING ALICE NAME AS DT

current_date=dt.date.today()
print('current date : ',current_date)

current_datetime=dt.datetime.now()
print('current time : ',current_datetime)

new=dt.datetime(2021,10,25)
print(new)
print('year : ',new.year)
print('month : ',new.month)
print('day : ',new.day)
a=dt.time(10,45,5,555505)
print(a)
print('hour : ',a.hour)
print('minute : ',a.minute)
print('second : ',a.second)
print('microsecond :',a.microsecond)

current_date=dt.datetime.now()
print('current time : ',current_date)

new=dt.datetime(2021,5,31,12,2,10)
print(new)
print(new.date())
print(new.time())

current=dt.datetime.now()
new_year=dt.datetime(2021,1,2)
difference=current-new_year
print('difference : ',difference)

current=dt.datetime.now()
print(current)
s=current.strftime('%A %B %D %Y')
print(s)