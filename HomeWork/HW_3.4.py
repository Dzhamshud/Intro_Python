# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num_dec = int(input('Введите десятичное число: '))
num_bin = ''
while num_dec > 0:
    ost = num_dec % 2
    num_bin = str(ost) + num_bin
    num_dec = num_dec // 2
print(f'Двоичное число {num_bin}')
