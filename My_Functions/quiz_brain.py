class QuizBrain:

    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0
    def keep_going(self):
        return self.q_number < len(self.q_list)

    def next_question(self):
        current_q = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number}: {current_q.text} (True/False): ")
        self.check_answer(user_answer, current_q.answer)

    def check_answer(self, input, correct):
        if input.lower() == correct.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You didn't get it right")
        print(f"Correct answer: {correct}")
        print(f"Your current score is: {self.score}/{self.q_number}")
        print("\n")
