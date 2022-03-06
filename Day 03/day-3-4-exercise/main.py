# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total_bill = 0

if size == "s":
	total_bill += 15
	if add_pepperoni == "y":
		total_bill += 2
	if extra_cheese == "y":
		total_bill += 1
	print(f"Your final bill is: {total_bill}")

elif size == "m":
	total_bill += 20
	if add_pepperoni == "y":
		total_bill += 3
	if extra_cheese == "y":
		total_bill += 1
	print(f"Your final bill is: {total_bill}")

elif size == "l":
	total_bill += 25
	if add_pepperoni == "y":
		total_bill += 3
	if extra_cheese == "y":
		total_bill += 1
	print(f"Your final bill is: {total_bill}")