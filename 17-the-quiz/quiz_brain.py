# Quiz logic class
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q.{self.question_number}: {current_question.text} (True/False)?\n> ")
        self.check_answer(user_input, current_question.answer)
        return current_question

    def check_answer(self, user_answer, correct_answer):
        if user_answer.strip().title() == correct_answer:
            self.score += 1
            print("¡Correcto! 🎉")
        else:
            print(f"Incorrecto 😢. The correct answer was: {correct_answer}")
        print(f"Score: {self.score}/{self.question_number}\n")
