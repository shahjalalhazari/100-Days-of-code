import time
import requests
from datetime import datetime
import smtplib

MY_LAT = 25.204849
MY_LONG = 55.270782

MY_EMAIL = "my_email@gmail.com"
PASSWORD = "dummypassw0rd"


def iss_overhead():
    """This function is responsible to my position is within +5 or -5 degrees of the ISS position."""
    # Get ISS current location and others info this API.
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # Raise Error if it has.
    response.raise_for_status()
    # Convert data in json formate
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # Check my position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    """This function will check is this is nighttime or not."""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    # Get my current time.
    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    # Run while loop every 60 minutes.
    time.sleep(60)
    if iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Look Up.\n\nThe ISS is above in the sky."
            )
