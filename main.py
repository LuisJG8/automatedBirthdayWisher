import smtplib
import random
import datetime
import pandas

EMAIL = "EMAIL"
PASSWORD = "PASSWORD"

the_date = datetime.datetime.today()
todays = the_date.day
todays_year = the_date.year
todays_month = the_date.month
mylist = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
print(the_date, todays_month, todays_year)

mycsv = pandas.read_csv("birthdays.csv")


p_dict = mycsv.to_dict()
print(p_dict)
print(p_dict["month"])
print(p_dict["day"])

for index, row in mycsv.iterrows():
    if (todays == row["day"]
            and todays_month == row["month"]):
        random_letter = random.choice(mylist)
        with open(f"{random_letter}") as my_letter:
            opening = my_letter.readlines()
            for i in opening:
                new_letter = i.replace("[NAME]", row["name"])
                print(new_letter)

        the_connection = smtplib.SMTP("smtp.gmail.com", port=587)
        the_connection.starttls()
        the_connection.login(user=EMAIL, password=PASSWORD)

        the_connection.sendmail(from_addr="Email", to_addrs="Email", msg=f"{new_letter}")