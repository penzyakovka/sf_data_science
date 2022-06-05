"""Игра "Угадай число".
   Компьютер сам загадывает и сам угадывает число.
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Угадываем число с помощью генератора случайных чисел.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток.
    """
    
    count = 0  #счетчик количества попыток
    min_number = 1  #левая граница области поиска
    max_number = 100  #правая граница области поиска
    
    while True:
        count += 1
        predict_number = np.random.randint(min_number, max_number + 1)  #предполагаемое число
        slim_number = int((max_number - min_number + 1)/2)  #значение для сужения области поиска
        
        if number > min_number + slim_number - 1:  #проверка для сдвига левой границы
            min_number += slim_number  #сдвиг левой границы области поиска
        
        elif number < min_number + slim_number - 1:  #проверка для сдвига правой границы
            max_number = max_number - slim_number - 1  #сдвиг правой границы области поиска
        
        if number == predict_number:  #выход, угадали число
            break
    
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм.

    Args:
        random_predict ([type]): Функция угадывания.

    Returns:
        int: Среднее количество попыток.
    """
    count_ls = []  #список для количества попыток угадывания
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))  #усреднили количество попыток
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток.")
    return score


if __name__ == "__main__":
    score_game(random_predict)
