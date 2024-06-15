def run(GAME_DESCRIPTION):
    print("Welcome to the Brain Games!")
    print(GAME_DESCRIPTION)
    player_name = input("May I have your name? ")
    print(f"Hello, {player_name}!")
    return player_name


def get_answer(question):
    print(f"Question: {question}")
    answer = input("Your answer: ")
    return answer
