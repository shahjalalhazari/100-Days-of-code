from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class GameInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        """WINDOW"""
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        """Score Text"""
        self.score_label = Label(
            text=f"Score: {self.quiz.score}",
            font=("Arial", 13, "normal"),
            fg="white", bg=THEME_COLOR
        )
        self.score_label.grid(column=1, row=0)
        """CANVAS"""
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.q_text = self.canvas.create_text(
            150, 125,
            width=260,
            text="Here is your question.",
            font=("Arial", 13, "italic"),
            fill=THEME_COLOR,
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=40)
        """RIGHT AND WRONG BUTTONS"""
        # True Button
        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img, command=self.true_answer, highlightthickness=0)
        self.true_btn.grid(column=0, row=2)
        # False Button
        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img, command=self.false_answer, highlightthickness=0)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """This method is responsible for Get Next Questions."""
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=q_text)
        else:
            self.canvas.itemconfig(self.q_text, text="You've reached the end of the quiz.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_answer(self):
        self.show_feedback(self.quiz.check_answer("True"))

    def false_answer(self):
        self.show_feedback(self.quiz.check_answer("False"))

    def show_feedback(self, is_true):
        if is_true:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)