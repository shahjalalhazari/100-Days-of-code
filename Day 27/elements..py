from tkinter import *

window = Tk()  # Create new tkinter object as window.
window.title("First GUI Program")  # Create title for this program.
window.minsize(width=500, height=300)  # Minimum size of the window

# Label
my_label = Label(text="This is a label.", font=("Arial", 12, "bold"))
# We can't see any Label, if we don't use pack method.
my_label.pack()  # ByDefault pack display text at top-center, but we can change text position with "side"
# parameter.

my_label["text"] = "My new label"  # To change current label.
my_label.config(text="My new label")  # Update the label


# Button
def button_clicked():
    input_text = my_input.get()  # Get inputted text
    my_label.config(text=input_text)  # Display inputted text as label


button = Button(text="Continue", command=button_clicked)  # command is use as like event listener.
# We can't see any Button, if we don't use pack method.
button.pack()


# Entry as Input
my_input = Entry(width=50)  # Define an input field with 50px width.
# Add some text to begin with
my_input.insert(END, string="Some text to begin with.")
# Gets text in entry
print(my_input.get())
my_input.pack()

# Text
text = Text(height=5, width=35)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


# Spinbox
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value.
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()
