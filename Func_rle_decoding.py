# Функция для восстановления сжатых данных 

def rle_decoding(data):
    decode_rle = ''
    count = ''
    for char in data:
        if char in data:
            if char.isdigit():
                count +=char
            else:
                decode_rle += char * int(count)
                count = ''
    return decode_rle