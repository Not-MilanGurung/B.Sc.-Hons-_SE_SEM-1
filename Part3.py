#Getting the current date
import datetime
current_year = datetime.date.today().year
current_month = datetime.date.today().month
current_day = datetime.date.today().day

#Calculating no. of seconds in a day, and a year without leap day
numsecs_day = (24) * (60) * (60)
numsecs_year = (365) * numsecs_day
#Calculating average number of seconds in a year,  and a month
avg_numsecs_year = ((4 * numsecs_year) + numsecs_day) // 4
avg_numsecs_month = avg_numsecs_year // 12 

#Input from the user
year_birth = int(input("Enter your birth year: "))
month_birth = int(input("Enter your birth month: "))
day_birth = int(input("Enter your day of birth: "))

#Calulating the result as the variables' name imply
numsecs_1900_to_dob = (year_birth - 1900) * avg_numsecs_year + (month_birth - 1) * avg_numsecs_month + (day_birth * numsecs_day)
numsecs_1900_to_today = (current_year - 1900) * avg_numsecs_year + (current_month - 1) * avg_numsecs_month + (current_day * numsecs_day)
age_in_secs = numsecs_1900_to_today - numsecs_1900_to_dob

print(f"You are {age_in_secs} seconds old")