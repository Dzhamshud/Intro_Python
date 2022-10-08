# Программа получает на вход значения 1, 4, 8, 7, 5 и находит среди них максимальное

num = [int(i) for i in input().split()]

#num = [1, 4, 8, 7, 5]
# max_ = num[0]
# for elem in num[1:]:
#     if elem > max_:
#         max_ = elem
# print(max_)

print(max(num))
