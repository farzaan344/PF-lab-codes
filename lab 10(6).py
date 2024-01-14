print("Farzaan Bin Khawar\n2023F-BIT-030")
import random

def guess_the_capitals():
    state_capitals = {
        "Alabama": "Montgomery",
        "Alaska": "Juneau",
        "Arizona": "Phoenix",
        "Arkansas": "Little Rock",
    }


    correct_responses = 0
    incorrect_responses = 0

    states = list(state_capitals.keys())
    while True:
        random_state = random.choice(states)
        user_guess = input(f"What is the capital of {random_state}? ").capitalize()

        if user_guess == state_capitals[random_state]:
            print("Correct!\n")
            correct_responses += 1
        else:
            print(f"Incorrect. The capital of {random_state} is {state_capitals[random_state]}.\n")
            incorrect_responses += 1
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    print("\nGame Over")
    print(f"Correct Responses: {correct_responses}")
    print(f"Incorrect Responses: {incorrect_responses}")
guess_the_capitals()
