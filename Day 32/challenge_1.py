"""Objective: Send a motivational quote via email on the current weekday."""
import datetime as dt
import random
import smtplib


MY_EMAIL = "my_email@gmail.com"
PASSWORD = "dummypassw0rd"
TO_ADDR = "testing@gmail.com"


# ----- Get weekday ----- #
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    # ----- Open the quotes file ----- #
    with open(file="quotes.txt", encoding="'utf-8-sig'") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

    # ----- Send mail with smtp ----- #
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_ADDR,
            msg=f"Subject:Weekday Quote\n\n{quote.encode('utf-8')}"
        )