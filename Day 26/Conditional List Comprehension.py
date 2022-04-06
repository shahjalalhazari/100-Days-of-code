#  Conditional List Comprehension
#  The Format is: new_list = [new_item for item in list if test]

names = [
    "Alex", "Beth", "Caroline",
    "Dave", "Eleanor", "Freddie"
]

short_names = [name for name in names if len(name) < 5]
print(short_names)


# CHALLENGE 1: Make a list of names that has 5 or
#  more letter with all the name is UPPERCASE.
uppercase_names = [name.upper() for name in names if len(name) > 5]
print(uppercase_names)