# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

string = 'aaaaabbbbccccююююfffggggggggg'
# string = 'aabbbc'
print(f'Исходная строка: {string}')
def rle_compression(text):
    text_compression = ''
    counter = 1
    symbol = ''
    for char in string:
        if char != symbol:
            if symbol:
                text_compression += str(counter) + symbol
            counter = 1
            symbol = char
        else:
            counter += 1
    else:
        text_compression += str(counter) + symbol
        return text_compression



def rle_decompression(text):
    text_decompression = ''
    counter = ''
    for char in text:
        if char.isdigit():
            counter = int(char)
        else:
            text_decompression += char*counter
            counter = ''
    return text_decompression

print(f'Сжатие: {rle_compression(string)}')
new_text = rle_compression(string)
print(f'Восстановление: {rle_decompression(new_text)}')
