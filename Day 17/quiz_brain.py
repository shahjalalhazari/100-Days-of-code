class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0


    def still_has_questions(self):
        """To check there is still has any question or not."""
        return self.question_number < len(self.question_list)


    def next_question(self):
        """To generate new question."""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """It will check user inputed answer is corrent or not."""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("That's a wrong Answer")
        print(f"The corrent answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")