import smtplib
import datetime as dt
import random

MY_EMAIL = "nauris.gruduls@gmail.com"
MY_PASSWORD = "warlock"

print("Hi")
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday motivation\n\n{quote}"
        )























# import smtplib
#
# my_email = "nauris.gruduls@gmail.com"
# password = "warlock123"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="tezoriv@gmail.com",
#                         msg="Subject:Hello\n\nThis is the body of my email.")

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15)
# print(date_of_birth)