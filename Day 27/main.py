from tkinter import *

def button_clicked():
    input_text = my_input.get()  # Get inputted text
    my_label.config(text=input_text)  # Display inputted text as label


window = Tk()  # Create new tkinter object as window.
window.title("First GUI Program")  # Create title for this program.
window.minsize(width=500, height=300)  # Minimum size of the window


# Label
my_label = Label(text="This is a label.", font=("Arial", 12, "bold"))
# We can't see any Label, if we don't use pack method.
my_label["text"] = "My new label"  # To change current label.
my_label.config(text="My new label")  # Update the label
# my_label.pack()  # ByDefault pack display text at top-center, but we can change text position with "side"
# parameter.


# Button
button = Button(text="Continue", command=button_clicked)  # command is use as like event listener.
# We can't see any Button, if we don't use pack method.
# button.pack()


# Entry as Input
my_input = Entry(width=50)  # Define an input field with 50px width.
# Gets text in entry
print(my_input.get())
# my_input.pack()



""" CHALLENGE #2: """
label = Label(text="Label")
label.grid(column=0, row=0)

button = Button(text="Button")
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

input = Entry()
input.grid(column=3, row=2)



window.mainloop()
