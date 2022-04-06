#  List Comprehension
#  The Format is:
#  new_list = [new_item for item in list]

# CHALLENGE: 1,
#  Add 1 with all the elements of list.
numbers = [1,2,3,4,5]
new_list = [n + 1 for n in numbers]
print(new_list)

# Multiply each element by 3
new_list = [n * 3 for n in numbers]
print(new_list)

# CHALLENGE: 2,
#  Make a list of all letters of a string.
name = "Shahjalal"
new_list = [letter for letter in name]
print(new_list)

# CHALLENGE: 3,
# Make a list of range between 1 and 5 and multiply each items of list.
my_list = [num * 2 for num in range(1, 6)]
print(my_list)