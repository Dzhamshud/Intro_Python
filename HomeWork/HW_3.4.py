# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

dec = int(input('Введите десятичное число: '))
bin = ''
while dec > 0:
    ost = dec % 2
    bin = str(ost) + bin
    dec = dec // 2
print(f'Двоичное число {bin}')
