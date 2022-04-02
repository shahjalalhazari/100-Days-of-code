### READ FILE(s) START ###

# METHOD #1
from statistics import mode


file = open("my_file.txt") # Open the file
contents = file.read() # Read the file
print(contents)
file.close() # Close the file

# SECOND METHOD
with open("my_file.txt") as file: # By default a file open in read mode.
    # In this method we don't need to close the file manually.
    text = file.read()
    print(text)

### END ###



# WRITE FILE(s) START ###

with open("my_file 2.txt", mode="w") as file: # 'w' stands for WRITE.
    file.write("New Text")

### END ###


# APPEND FILE(s) START ###

with open("my_file 3.txt", mode="a") as file: # 'a' stands for APPEND.
    file.write("\nNew Text.")

### END ###