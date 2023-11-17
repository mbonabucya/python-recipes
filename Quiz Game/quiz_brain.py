
class QuizBrain:
    def __init__(self, qu_list):
        self.question_number = 0
        self.question_list = qu_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_score(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 10
            print('you got it right')

        else:
            print(f'sorry , that was wrong answer , The correct is : {correct_answer}')
        print(f'Current score: {self.score} out of {10 * self.question_number}')

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} True/False \n")
        self.check_score(user_answer, current_question.answer)