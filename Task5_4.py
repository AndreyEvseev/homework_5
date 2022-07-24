# Задание 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.  
# Входные и выходные данные хранятся в отдельных текстовых файлах.

work_file = 'files/f_data5_4_source.txt'
way = input('Если Вы хотите сгенерировать новый поток данных, введите 1,\n'
    'если нет - введите любое другое число: ')
if int(way) == 1:
    import Func_data_flow_generator as dfg
    dfg.data_flow_generator(work_file)

import Func_read_files as rf
incoming_stream = rf.read_file(work_file)

import Func_rle_encoding as rle_enc
compressed_data = rle_enc.rle_encoding(incoming_stream)

comprssed_file = 'files/f_data5_4_compressed.txt'
import Func_writing_file as wf
wf.writing_file(compressed_data, comprssed_file)

import Func_rle_decoding as dec
restored_data = dec.rle_decoding(compressed_data)

recovered_file = 'files/f_data5_4_recovered.txt'
wf.writing_file(restored_data, recovered_file)
