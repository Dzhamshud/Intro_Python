# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# string = 'aaaaabbbbccccююююfffggggggggg'
string = 'aabbbc'
str_list = list(string)
print(str_list)
new_string = ''
for elem in range(len(str_list)-1):
    print(str_list[elem], end='')
    print(str_list[elem+1], end='')
#     counter = 1
#     if str_list[elem] == str_list[elem+1]:
#         counter +=1
#     else:
#         elem_end = str_list[elem]
#         if counter >1:
#             print(counter)
#             new_string = new_string + str(counter)
#         new_string = new_string + str(elem_end)
# print(new_string)
        
