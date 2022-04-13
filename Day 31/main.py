from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ----- READ CSV FILEs ----- #
current_card = {}
try:
    data = pandas.read_csv("data/known_words.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    words = original_data.to_dict(orient="records")
    # This 'orient="records"' converts DataFrame into a List of Dictionaries of each column.
else:
    words = data.to_dict(orient="records")


def next_card():
    """This function is responsible for read data from csv file and display word on cards."""
    global current_card, flip_time
    window.after_cancel(flip_time)
    current_card = random.choice(words)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_img)
    flip_time = window.after(5000, func=flip_card)


def flip_card():
    """This function will flip the card and show English word(s) of French word(s)."""
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_img)


def known_words():
    """This function will handle known word(s). Means it will remove all the known words from
    main csv file and store in another csv file."""
    words.remove(current_card)
    known_word_list = pandas.DataFrame(words)
    known_word_list.to_csv("data/known_words.csv", index=False)
    # 'index=False' will turn off automatic indexing.

    next_card()


# ----- UI ----- #
""" MAIN WINDOW """
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_time = window.after(5000, func=flip_card)


""" CANVAS """
canvas = Canvas(width=800, height=526)
# Cards
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_img)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
# Texts on card(s)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 35, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 45, "bold"))


#  BUTTONS
# Cross Button
cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img, command=next_card)
unknown_button.grid(column=0, row=1)
# Check Button
check_img = PhotoImage(file="images/right.png")
known_button = Button(image=check_img, command=known_words)
known_button.grid(column=1, row=1)
# Call our next card function to get a word from csv at first.
next_card()

window.mainloop()
