#-----------------------Age Calculator-----------------------
import calendar
from datetime import datetime

#--------------------------main logic------------------------
#________to calculate age________
def calculate_age(birth_date,current_date):
    #_____________to calculate years____________
    years=(current_date.year - birth_date.year) - 1
    #____________to calculate months_____________
    m=current_date.month - birth_date.month
    if m<0:
        month=12+m
    else:
        month=12-m
    #___________to calculate days_______________
    d=current_date.day - birth_date.day
    if d<0:
        #get previous month and year
        if current_date.month == 1:
            pre_month=12
            year=current_date.year - 1
        else:
            pre_month=current_date.month - 1
            year=current_date.year

        #get number of days in previous month
        days_in_pre_month=calendar.monthrange(year,pre_month)[1]
        day=days_in_pre_month + d
    else:
        day=d
    
    return years,month,day 

#--------------------------input from user---------------------
print(f"******WLECOME TO AGE CALCULATOR*******")
name=input("Enter your name : ")
birth_input=input("Enter your date of birth in (YYYY-MM-DD) format : ")
try:
    birth_date=datetime.strptime(birth_input,"%Y-%m-%d")
    current_date=datetime.now()

    if birth_date>current_date:
        print("Birth date can not be in future")
    else:
        y,m,d=calculate_age(birth_date,current_date)
#__________________________display output_____________________
        print(f"HELLO! {name}, you are {y} years {m} months and {d} days old")
except ValueError:
    print("Invalid format Please enter in (YYYY-MM-DD) format!")

#--------------------------END OF PROGRAM--------------------
