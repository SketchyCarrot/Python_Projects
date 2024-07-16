from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    q_txt = q["text"]
    q_ans = q["answer"]
    new_q = Question(q_txt, q_ans)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.keep_going():
    quiz.next_question()

print("You have comoleted the quiz!")
print(f"Your final score: {quiz.score}/{quiz.q_number}")
