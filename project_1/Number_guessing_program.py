"""
Компьютер загадывает число, а затем пытается его угадать за наименьшее количество попыток и подсчитывет среднее количество попыток.
"""

from random import random
import numpy as np

def random_funс():
    
    """
    Функция задает рандомное число от 1 до 100. 
    
    """
    random_number = np.random.randint(1, 101)
    return random_number


def guessing_funс ():    
    
    """
    Функция на входе по умолчанию загадывает число. 
    Затем в теле функции пыается угадать его максимально быстрам способом. 
    После каждой попытки угадать функция узнает больше ли ответ загаданного числа или меньше. 

    Returns:
        function: количество попыток, затраченных на угадывание
    """    

    number = random_funс ()
  
    count = 0 #Количество попыток
    lst_numbers = list(range(1, 101)) #Список, который нужен для определения половины значений. 
    hulf_lst = 0

    while True:
        count += 1
        hulf_lst = int(len(lst_numbers)/2) #Определение среднего элемента списка
        predict_number = lst_numbers[hulf_lst] #Среднее значение списка
        if predict_number > number:
            lst_numbers = lst_numbers[:hulf_lst]
        elif predict_number < number:
            lst_numbers = lst_numbers[hulf_lst:]
        else:
            break # Если мы угалали, прерываем список
    return count # Выводим количество попыток. 


def score_func (guessing_funс): 
    """
    Функция подсчета среднего количества попыток за 1000 циклов.

    Args:
        guessing_fun (function): Функция передает количество попыток

    Returns:
        int: Среднее число
    """    
    
    count_ls = []
    
    number_of_attempts = 1000
    for attempt in range(1, number_of_attempts+1):
        count_ls.append(guessing_funс())
    
    
    score = int(np.mean(count_ls))
    return print(f'Your algorithm guesses the number on average for: {score} attempts')

score_func(guessing_funс)