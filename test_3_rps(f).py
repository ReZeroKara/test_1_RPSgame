# Игра Камень, Ножницы, Бумага. Написаная с помощью функций

import random
from enum import IntEnum


# Связываем каждый вариант фигуры в игре с числом
class Var(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

# Функция для получения выбора игрока
def get_player_choice():
    choices = [f"{action.name}[{action.value}]" for action in Var]
    choices_str = ", ".join(choices)
    selection = int(input(f"Сделайте выбор — ({choices_str}): "))
    action = Var(selection)
    return action

# Получаем вариант компьютера
def get_computer_choice():
    choice = random.randint(0, len(Var) - 1)
    action = Var(choice)
    return action

# Функция для определения победителя
def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        print(f"Оба пользователя выбрали {user_action.name}. Ничья!")
    elif user_action == Var.Rock:
        if computer_action == Var.Scissors:
            print("Камень бьет ножницы! Вы победили!")
        else:
            print("Бумага оборачивает камень! Вы проиграли.")
    elif user_action == Var.Paper:
        if computer_action == Var.Rock:
            print("Бумага оборачивает камень! Вы победили!")
        else:
            print("Ножницы режут бумагу! Вы проиграли.")
    elif user_action == Var.Scissors:
        if computer_action == Var.Paper:
            print("Ножницы режут бумагу! Вы победили!")
        else:
            print("Камень бьет ножницы! Вы проиграли.")

# Собственно цикл игры, будет продолжаться пока игрок её не остановит
while True:
    try:
        user_action = get_player_choice()
# Защита от неправильного ввода;)
    except ValueError as e:
        range_str = f"[0, {len(Var) - 1}]"
        print(f"Некорректный ввод. Введите значение из промежутка {range_str}")
        continue
    computer_action = get_computer_choice()
    determine_winner(user_action, computer_action)
    play_again = input("Сыграем еще? (да/нет): ")
    if play_again.lower() != "да":
        break