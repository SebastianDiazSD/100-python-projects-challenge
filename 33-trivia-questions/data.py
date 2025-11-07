import requests
import random
import html
from question_model import Question

# 🎯 Fetch only multiple-choice questions from Open Trivia DB
response_trivia = requests.get(
    url="https://opentdb.com/api.php?amount=50&type=multiple",
    timeout=10
)
response_trivia.raise_for_status()

# Convert the response into JSON format
data = response_trivia.json()
trivia_database = data["results"]

question_bank = []
for question in trivia_database:
    question_text = html.unescape(question["question"])
    correct_answer = html.unescape(question["correct_answer"])
    incorrect_answers = [html.unescape(a) for a in question["incorrect_answers"]]

    # Combine and randomize the answer choices
    all_choices = incorrect_answers + [correct_answer]
    random.shuffle(all_choices)

    question_category = html.unescape(question["category"])
    new_question = Question(
        q_text=question_text,
        q_answer=correct_answer,
        q_category=question_category,
        q_choices=all_choices
    )
    question_bank.append(new_question)
