from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    check_mark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """This function is responsible for count our times."""
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    #  if it's the 8th rep
    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text="Break", fg=RED)
    #  if it's the 2nd,4th & 6th rep
    if reps % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Break", fg=PINK)
    #  If it's the 1st,3rd,5th & 7th rep
    else:
        count_down(work_sec)
        title.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """This function is responsible for time count down."""
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    '''Before we used "config" for update anything but now we can't, Cuz now we have to update a particuler item.
    That's why we're using "itemconfig" method.'''
    if count > 0:
        '''1000 means 1000 milliseconds or 1 second'''
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

#  Window
window = Tk()
window.title("Pomodoro")
'''padx stands for Padding X and pady for Padding Y.'''
window.config(padx=100, pady=75, bg=YELLOW)

#  Title Label
title = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 45, "normal"))
title.grid(column=1, row=0)

#  Canvas
'''highlightthickness=0 is for remove border of images. '''
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
'''PhotoImage takes file path of images.'''
canvas.create_image(100, 112, image=tomato_img)
'''image can't take direct any path of files, that's why we've to provide a variable as image parameter. '''
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 25, "bold"))  # fill is for fill color.
canvas.grid(column=1, row=1)

#  Start Button
start_button = Button(text="Start", command=start_timer, padx=10, pady=5, bg=GREEN, fg="black", highlightthickness=0)
start_button.grid(column=0, row=2)

#  Reset Button
reset_button = Button(text="Reset", command=reset_timer, padx=10, pady=5, bg=RED, fg="white", highlightthickness=0)
reset_button.grid(column=2, row=2)

#  check-Marks Label
check_mark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
check_mark.grid(column=1, row=3)

window.mainloop()
