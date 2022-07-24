# Функция RLE сжатия 

def rle_encoding(data):
    encode_rle = ''
    prev_char = ''
    count = 1
    if not data: return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encode_rle += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encode_rle += str(count) + prev_char
    return encode_rle