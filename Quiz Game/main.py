from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    qu_text = question["text"]
    qu_answer = question["answer"]
    que_object = Question(qu_text, qu_answer)
    question_bank.append(que_object)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

