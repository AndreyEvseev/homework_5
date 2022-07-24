# Функция для генерации случайного потока повторяющихся данных

import random

def data_flow_generator(user_file: str):
    number_characters = random.randint(5, 20)
    simbol_str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    data_flow = ''
    for i in range(number_characters):
        simbol_flow = random.choice(simbol_str)
        number_repetitions = random.randint(1, 50)
        for j in range(number_repetitions):
            data_flow += simbol_flow
    import Func_writing_file as wf
    wf.writing_file(data_flow, user_file)
    return data_flow