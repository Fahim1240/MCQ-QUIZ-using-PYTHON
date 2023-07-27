import random


def ask_name():
    name = input("Please enter your name: ")
    return name


def display_question(question, choices):
    print(question)
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")
    user_choice = int(input("Enter the number of your choice (1, 2, 3, or 4): "))
    return user_choice

def check_answer(user_choice, correct_answer):
    return user_choice == correct_answer


def update_high_score(name, score):
    with open("high_scores.txt", "a") as file:
        file.write(f"{name}: {score}\n")