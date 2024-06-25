import random


DESCRIPTION = "What number is missing in the progression?"


def get_question_and_answer():
    first_number = random.randint(1, 20)
    step = random.randint(1, 5)
    progression = [first_number]
    for n in range(10):
        progression.append(progression[-1] + step)
    hidden_index = random.randint(0, 9)
    answer = str(progression[hidden_index])
    progression[hidden_index] = ".."
    question = (' '.join(map(str, progression)))
    return question, answer
