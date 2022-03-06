#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))

# percentage of tip
tip_in_pers = tip / 100
# percentage of bill
pers_of_bill = bill * tip_in_pers
# total bill
total_bill = bill + pers_of_bill
# Pay each person
for_each_person = round(total_bill / people, 2)
print(f"Each person should pay ${for_each_person}")