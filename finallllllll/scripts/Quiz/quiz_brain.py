
class QuizBrain:
    def __init__(self, q_list):
        self.question_list=q_list
        self.question_number=0
        self.score=0
        self.attempt=0

    def next_question(self):
        next_q=self.question_list[self.question_number]
        self.question_number +=1
        choice=input(f"Q.{self.question_number} {next_q.text} (True/False)?")
        self.check_answer(choice, next_q)

    def still_has_questions(self):
        if self.question_number<len(self.question_list):
            return True
        else:
            return False

    def check_answer(self,user_ans, nextq):
        self.attempt+=1
        if user_ans.lower()==nextq.answer.lower():
            print("You got it right!")
            self.score+=1
            print(f"Score: {self.score}/{self.attempt}")
        else:
            print("That's wrong!")
            print("The correct answer was ", nextq.answer)
