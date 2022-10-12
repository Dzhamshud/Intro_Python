# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов. Для N = 5: 1, -3, 9, -27, 81 и т.д.
# from random import randint
# n = int(input('введите число '))
# lst = []
# if n == 5:
#     for i in range(n):
#         lst.append((-3)**i)
# else:
#     for i in range(n):
#         lst.append(randint(1, 10))
# print(lst)

n = int(input('введите число '))
lst = [1]
i = 1
while i < n:
    num = lst[-1]*(-3)
    lst.append(num)
    i = i+1
print(lst)
