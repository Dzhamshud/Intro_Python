# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

f = int(input('Введите искомое число: '))
my_list = [1, 'result', 3, 5, 8, 9, 'list']
cnt = 0
for i in range(len(my_list)):
    if my_list[i] == f:
        print(f'В списке присутствует число {f} на позиции {i+1}')
        cnt += 1

if cnt == 0:
    print(f'В списке нет числа {f}')
