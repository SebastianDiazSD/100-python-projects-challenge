import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Loads next question and returns its text."""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def question_choices(self):
        """Returns a list of choices for the current question."""
        return [html.unescape(choice) for choice in self.current_question.choices]

    def check_answer(self, user_answer):
        """Compares user answer with correct answer."""
        correct_answer = self.current_question.answer
        if user_answer.strip().lower() == correct_answer.strip().lower():
            self.score += 1
            return True
        return False
