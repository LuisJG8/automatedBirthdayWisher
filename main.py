##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

import smtplib
import random
import datetime
import pandas

the_date = datetime.datetime.today()
todays = the_date.day
todays_year = the_date.year
todays_month = the_date.month
mylist = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
print(the_date, todays_month, todays_year)

mycsv = pandas.read_csv("birthdays.csv")
my_tupil = (todays_year, the_date)


p_dict = mycsv.to_dict()
print(p_dict)
print(p_dict["month"])
print(p_dict["day"])

for index, row in mycsv.iterrows():
    if (todays == row["day"]
            and todays_month == row["month"]):
        random_letter = random.choice(mylist)
        with open(random_letter) as my_letter:
            opening = my_letter.readlines()
            

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.