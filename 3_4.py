import random

correct_answers = 0
mistakes = 0

while mistakes < 3:
    n1 = random.randint(1, 10)
    n2 = random.randint(1, 10)
    answer = n1 + n2

    user_answer = int(input(f"{n1} + {n2} = "))

    if user_answer == answer:
        print("Правильно!")
        correct_answers += 1
    else:
        print("Ответ неверный")
        mistakes += 1

print(f"Игра окончена. Правильных ответов: {correct_answers}")