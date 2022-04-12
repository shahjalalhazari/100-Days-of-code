#  FileNotFound
try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["key"])
except FileNotFoundError:
    '''We can hold error message for a particular work.'''
    file = open("a_file.txt", "w")
    file.write("SHAHJALAL HAZARI")
except KeyError as error_message:
    '''Hold the error message into error_message'''
    print(f"The Key {error_message} doesn't exist.")
else:
    data = file.read()
    print(data)
finally:
    '''No matter what happened in other blocks. This block of code will run.'''
    file.close()
    print("The file is closed.")
    #  Raise error(s)
    '''If we raise our own error, Still it will raise the error.'''
    raise IndexError


#  Raise an error form scratch
height = float(input("Your Height: "))
weight = int(input("Your Weight: "))

if height > 2.5:
    raise ValueError("Human height should not be over 2.5 meters.")

bmi = weight / height ** 2
print(bmi)