# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
from random import randint
n = int(input('введите число '))

for i in range(n):
    i = randint(1, 100)
    print(i, end=' ')
