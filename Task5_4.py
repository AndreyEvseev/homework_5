# Задание 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.  
# Входные и выходные данные хранятся в отдельных текстовых файлах.

import Func_data_flow_generator as dfg
import Func_read_files as rf
import Func_rle_encoding as rle_enc
import Func_writing_file as wf
import Func_rle_decoding as dec

def cleared(comprssed_file, recovered_file):
    if int(input('Для очистки рабочих файлов введите 0.\n'
        'Для сохранения - другое число: ')) == 0:
        cleared_data = ''
        cleared_file = comprssed_file
        wf.writing_file(cleared_data, cleared_file)
        cleared_file = recovered_file
        wf.writing_file(cleared_data, recovered_file)

work_file = 'files/f_data5_4_source.txt'
comprssed_file = 'files/f_data5_4_compressed.txt'
recovered_file = 'files/f_data5_4_recovered.txt'
cleared(comprssed_file, recovered_file)

way = input('Если Вы хотите сгенерировать новый поток данных, введите 1,\n'
    'если нет - введите любое другое число: ')
if int(way) == 1:
    dfg.data_flow_generator(work_file)

incoming_stream = rf.read_file(work_file)

compressed_data = rle_enc.rle_encoding(incoming_stream)

wf.writing_file(compressed_data, comprssed_file)

restored_data = dec.rle_decoding(compressed_data)

wf.writing_file(restored_data, recovered_file)

cleared(comprssed_file, recovered_file)
