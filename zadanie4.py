file4 = open('questions.txt','r',encoding='UTF-8')
file5 = open('answers.txt','r',encoding='UTF-8')
score = 0

questions = file4.readlines()
answers = file5.readlines()

for i in range(len(questions)):
    user_answer = input(questions[i])

    if user_answer.strip().lower() == answers[i].strip().lower():
        score += 1
file4.close()
file5.close()
print("Вы ответили правильно на {} вопросов из 10.".format(score))