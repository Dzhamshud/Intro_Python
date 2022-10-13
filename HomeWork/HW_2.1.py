# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

num = float(input('Введите число '))
st = str(num)
st.split()
sum = 0
for i in range(len(st)):
    if st[i] != '.':
        if st[i] != '-':
            sum = sum + int(st[i])
print(sum)
