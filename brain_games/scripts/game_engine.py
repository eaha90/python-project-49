import argparse
import importlib
import prompt


def launch_game(game_module):
    """
    Запускает игру.

    Args:
        game_module: Модуль игры с функциями generate_question, check_answer.
    """
    print("Welcome to the Brain Games!")
    print(game_module.GAME_DESCRIPTION)
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    # Количество правильных ответов
    correct_answers_count = 0

    # Количество раундов для победы
    rounds_to_win = 3

    # Цикл, пока не будет достигнуто нужное количество правильных ответов
    while correct_answers_count < rounds_to_win:
        # Получаем вопрос и правильный ответ из модуля игры
        question, correct_answer = game_module.generate_question()

        # Выводим вопрос
        print(f"Question: {question}")

        # Запрашиваем ответ пользователя
        user_answer = prompt.string("Your answer: ")

        # Проверяем ответ
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'"
            )
            print(f"Let's try again, {name}!")
            break

    # Выводим сообщение о победе
    if correct_answers_count == rounds_to_win:
        print(f"Congratulations, {name}!")


def main():
    parser = argparse.ArgumentParser(description='Play Brain Games!')
    parser.add_argument('game', choices=['calc', 'even', 'gcd', 'prime', 'progression'],
                        help='Name of the game to play.')
    args = parser.parse_args()

    # Динамический импорт модуля игры
    game_module = importlib.import_module(f"brain_games.games.{args.game}")

    # Запуск игры
    launch_game(game_module)


if __name__ == '__main__':
    main()
