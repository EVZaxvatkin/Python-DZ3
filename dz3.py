# 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

# Пример:

#  [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


#n = [2, 3, 5, 9, 3] 

#print(f'Ответ: {sum([n[i] for i in range(1, len(n), 2)])}')


#__________________________________________________________________________________________________________________________________

#   2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
# 



# n = [2, 3, 4, 5, 6]

#print()

#lst_1 = []
#if len(n) %2 == 0:
#     for i in range(len(n)//2):
#         mul = n[i] * n[(i+1)*-1]
#         lst_1.append(mul)
        
#else:
#     for i in range((len(n)//2)+1):
#         mul = n[i] * n[(i+1)*-1]
#         lst_1.append(mul)
            
#print(lst_1)

#________________________________________________________________________________________________________

#   3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


#def convert(arr):
#     return [arr[i] % 1 for i in range(len(arr))]
    
#n = [1.1, 1.2, 3.1, 5, 10.01]

#print(int((max(convert(n)) - min(convert(n))) * 100) / 100)
    
#_________________________________________________________________________________________________________

#   4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

#n = int(input('Введите число: '))

#def binary(n):
#    b = ''
#    while n>0:
#        b= str(n%2) + b
#        n = n//2
#    return int(b)

#print(binary(n))

#__________________________________________________________________________________________________________

# Доп задача

# 5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Доп)

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]



#def fibb(n):
#    lst = []
#    f1, f2 = 1, 1
#    for i in range(abs(n)):
#        lst.append(f1)
#        f1, f2 = f2, f1 + f2
#    return lst
        
#def neg_fibb(n):
#    lst = []
#    f1, f2 = 1, -1
#    for i in range(abs(n)):
#        lst.append(f1)
#        f1, f2 = f2, (f1 + 1) - (f2 + 1)
#    return lst
    

#n = 8

#print(neg_fibb(n)[::-1] + [0] + fibb(n))


