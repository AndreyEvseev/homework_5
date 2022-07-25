# Задание 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

def func_transfrom_text(simbols: list, source_text: str) -> list:
    transfrom_text = source_text
    transfrom_text = transfrom_text.replace('\n', '\\n ')
    for item in range(len(simbols)):
        transfrom_text = transfrom_text.replace(simbols[item], ' ' + simbols[item]) 
    while transfrom_text.count('  ') != 0:
        transfrom_text = transfrom_text.replace('  ', ' ')
    transfrom_text = transfrom_text.split()
    return transfrom_text

def func_exclude_text(exclude_str: str, option: int, transfrom_text: list) -> list:
    exclude_list = transfrom_text
    for el in transfrom_text:
        if option == 1:
            if exclude_str.lower() in el.lower():
                exclude_list.remove(el) 
        else:
            if exclude_str in el:
                exclude_list.remove(el) 
    return exclude_list

def new_name(simbols):
    return [' ' + item for item in simbols]

def recovery_exclude_text(exclude_list: list, simbols: list) -> str:
    exclude_text = " ".join(exclude_list)
    simbols2 = new_name(simbols)
    for item in range(len(simbols2)):
        exclude_text = exclude_text.replace(simbols2[item], simbols[item]) 
    exclude_text = exclude_text.replace('\\n ', '\n')
    return exclude_text

exclude_str = 'абв'
simbols = ['.', ',', ':', ';', '!', '?', '\\n']
work_file = 'files/f_text5_1_course.txt'
import Func_read_files as rf
source_text = rf.read_file(work_file)
option = int(input('Если слова нужно удалить без учёта регистра, введите 1.\n'
    'Если нужно учитывать регистр, введите любое другое число: '))
transfrom_text = func_transfrom_text(simbols, source_text)
exclude_list = func_exclude_text(exclude_str, option, transfrom_text)
exclude_text = recovery_exclude_text(exclude_list, simbols)

exclude_file = 'files/f_text5_1_exclude.txt'
# Сохраняем результат в текстовый файл
import Func_writing_file as wf
wf.writing_file(exclude_text, exclude_file)
