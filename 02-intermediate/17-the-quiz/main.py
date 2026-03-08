from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

# Create Question objects from data
question_bank = []
for item in question_data:
    new_question = Question(item)
    question_bank.append(new_question)

# Shuffle for randomness
random.shuffle(question_bank)

# Start the quiz
quiz = QuizBrain(question_bank)

print("¡Bienvenido a tu Quiz de Python! 🇨🇴\n")

while quiz.still_has_question():
    quiz.next_question()

# Final score
print(f"¡Listo parcero! Your final score was {quiz.score}/{len(question_bank)}")
print("You have completed the quiz. Try it again to improve your score! 😎")