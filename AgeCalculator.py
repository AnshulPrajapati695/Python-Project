#-----------------------Age Calculator-----------------------
from datetime import date 
import time

#--------------------------main logic------------------------
#________to calculate years________
def year_calculate():
    print(f"******WLECOME TO AGE CALCULATOR*******")
    birth_year=int(input("Enter your birth year(e.g. 2005) : "))
    current_year=date.today().year
    year= current_year - birth_year
    return year

#_______to calculate months________
def month_calculate():
    month=date.today().month - 1
    return month

#_______to calculate days__________
def day_calculate():
    day=date.today().day - 1
    return day

#______to calculate hours__________
def hour_calculate():
    hour=time.localtime().tm_hour
    return hour

#______to calculate minutes_________
def minute_calculate():
    minute=time.localtime().tm_min
    return minute

#______to calculate seconds_________
def second_calculate():
    second=time.localtime().tm_sec
    return second

#--------------------------function call---------------------
name=input("Enter your name : ")
print(f"HELLO! {name}, you are {year_calculate()} years {month_calculate()} months {day_calculate()} days {hour_calculate()} hours {minute_calculate()} minutes and {second_calculate()} seconds old")

#--------------------------END OF PROGRAM--------------------
