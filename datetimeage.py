#ask for year

#ask for month

#ask for day 

#print out "You are x years old"

import datetime

year_birth = input("Insert Year of birth : " )
month_birth = input("Inser Month of birth : " )
day_birth = input("Insert Day of birth : ")

birth_date = datetime.date(year=int(year_birth), month=int(month_birth), day=int(day_birth))

today = datetime.date.today()

age = today - birth_date

print(round(age.days/365))

# you have been living in this world for x days
# you were born on x