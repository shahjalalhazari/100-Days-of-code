from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip


# ------------- PASSWORD GENERATOR ------------- #

def generate_password():
    """This function is responsible for Generate Password."""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    # Input generated password into Password Entry field.
    password_input.insert(0, password)
    #  Copy generated password while clicked in button.
    pyperclip.copy(password)


# ------------- SAVE PASSWORD ------------- #
def save_data():
    """This is function will save user inputs in a file."""
    # Get user inputted data.
    get_website = website_input.get()
    get_email = email_input.get()
    get_password = password_input.get()

    #  Check Website & Password field is blank or not
    if len(get_website) == 0 or len(get_password) == 0:
        #  If any field is blank
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any field empty.")
    else:
        is_ok = messagebox.askokcancel(
            title=get_website,
            message=f"these are the details entered \nEmail: {get_email}\nPassword: {get_password}, \nis it ok to save"
        )

        # Write saved_data file with new inputted data.
        if is_ok:
            with open("saved_data.txt", mode="a") as data:
                data.write(f"{get_website} | {get_email} | {get_password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)


# ------------- UI SETUP ------------- #
#  WINDOWS
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#  CANVAS
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#  LABELS
website_label = Label(text="Website:", font=("arial", 10, "normal"))
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", font=("arial", 10, "normal"))
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=("arial", 10, "normal"))
password_label.grid(column=0, row=3)

#  ENTRIES / INPUTS
website_input = Entry(width=55)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry(width=55)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "shahjalalhazari1@gmail.com")

password_input = Entry(width=36)
password_input.grid(column=1, row=3)

# BUTTONS
generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(column=2, row=3)

add = Button(text="Add", width=47, command=save_data)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
