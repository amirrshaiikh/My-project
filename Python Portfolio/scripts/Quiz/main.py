from data import question_data
from question_model import Question
from random import choice
from quiz_brain import *

question_bank= []
for acc in question_data:
    question_bank.append(Question(acc['text'], acc['answer']))

# print(question_bank)
# new_question=choice(question_bank)
qz= QuizBrain(question_bank)
#print(new_question.text)
while qz.still_has_questions():
    qz.next_question()

print("You have completed the quiz")
print(f"Your score was {qz.score}/{qz.attempt}")
