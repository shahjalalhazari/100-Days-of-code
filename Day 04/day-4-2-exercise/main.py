# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

# Get total length of list
total_names = len(names)

# Pick random name from list
random_person = random.randint(0, total_names - 1)

# Get random person's name
person = names[random_person]

# Print result
print(f"{person} is going to buy the meal today!")
