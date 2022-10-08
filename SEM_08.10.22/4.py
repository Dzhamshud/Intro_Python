# Показать первую цифру дробной части числа
# 6.85 -> 8

a = 6.85  # тип float
# a = a*10
# print(a)
# a = int(a)
# print(a)
# print(a%10)

st = str(a)  # предобразуем тип данных из float в string
print(st)
d = (st.find('.'))
print(st[d+1])
