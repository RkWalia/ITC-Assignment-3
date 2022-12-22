#Ques2

date=int(input("Enter a date: "))
month=int(input("Enter a month: "))
year=int(input("Enter a year: "))

if (year%400==0):
    leap_year=True
elif (year%100==0):
    leap_year=False
elif (year%4==0):
    leap_year=True
else:
    leap_year=False


if (month==1,3,5,7,8,10,12):
    no_of_days=31
elif (month==2):
    if leap_year==True:
        no_of_days=29
    else:
        no_of_days=28
else:
    no_of_days=30

if (date<no_of_days):
    date+=1
else:
    date=1
    if (month==12):
        month=1
        year+=1
    else:
        month+=1


print("The next date is [dd/mm/yyyy]",date,"/",month,"/",year)

