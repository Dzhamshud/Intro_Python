# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

txt = input('Введите текст через пробел: ')
print(f'Исходный текст: {txt}')
lst = [i for i in txt.split() if 'абв' not in i]
print(f'Результат: {" ".join(lst)}')