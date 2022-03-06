# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# convert user input into Floting Point Number
height = float(height)
weight = float(weight)

# get bmi of person's weight divided by square of height
bmi = weight / height ** 2
print(int(bmi))