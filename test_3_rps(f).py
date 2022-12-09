# Игра Камень, Ножницы, Бумага. Написаная с помощью функций

import random
from enum import IntEnum


class Var(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

def get_player_choice():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Сделайте выбор — ({choices_str}): "))
    action = Var(selection)
    return action