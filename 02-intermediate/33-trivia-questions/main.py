from data import question_bank
from quiz_brain import QuizBrain
from ui import QuizInterface

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
