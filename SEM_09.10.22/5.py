# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

from itertools import count


str1 = 'мир, привет, я первая строка! приветик'
str2 = 'привет'
index = -1
count = 0
while index < len(str1):
    index = str1.find(str2, index+1)
    if index == -1:
        break
    count += 1
print(count)
