import smtplib


my_email = "my_email@gmail.com"
password = "dummypassw0rd"
to_addrs = "testing@gmail.com"
#
# # ---- 1st Way ---- #
connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=120)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs=to_addrs,
    msg="Subject:Hello\n\nThis is my email body."
)
connection.close()


# ---- 2nd Way ---- #
with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=to_addrs,
        msg="Hello"
    )


import datetime as dt

now = dt.datetime.now()
print(now)
print(now.year)
print(now.day)
print(now.month)
print(now.hour)
print(now.weekday())

date_of_birth = dt.datetime(year=2001, month=11, day=10)
print(date_of_birth)