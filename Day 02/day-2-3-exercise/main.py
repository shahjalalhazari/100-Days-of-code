# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# get Remaining Years
remaining_years = 90 - int(age)
# 12 months of a year
remaining_months = remaining_years * 12
# 52 weeks a years
remaining_weeks = remaining_years * 52
# 365 days of a year
remaining_days = remaining_years * 365

# Print whole sentence
print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")