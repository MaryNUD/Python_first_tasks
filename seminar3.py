# Задача №1. Решение в группах Дан список чисел. 
# Определите, сколько в нем встречается различных чисел. 
# Input: [1, 1, 2, 0, -1, 3, 4, 4] 
# Output: 6

# list = [1, 1, 2, 0, -1, 3, 4, 4]
# print (f'Our list is: {list}')
# list = set(list)
# print (f'The number of unique elements is: {len(list)}')




# Задача №2. Решение в группах Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число. 
# Input: [1, 2, 3, 4, 5] k = 2 Output: [4, 5, 1, 2, 3]

# numbers = [1, 2, 3, 4, 5]
# print (numbers)
# k = int(input('Enter k value for shift: '))
# for i in range(k):
#     numbers.insert(i, numbers.pop())
# print (numbers) # works if k is 2


# numbers = [1, 2, 3, 4, 5]
# print (numbers)
# k = int(input('Enter k value for shift: '))
# new_list = numbers[-k:] + numbers[:-k]
# print (new_list)   # не будет работать, тк 5 должна быть 1ым элементом, а 4 вторым


# negafibonnachi 
# Задача 1 НЕГАФИБОНАЧЧИ по желанию
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 9 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


k = int(input('Enter k value to fix the size of the list: '))
negafib_pos = [0, 1] + [0] * (k - 2)
negafib_neg = [0, 1] + [0] * (k - 2)
for i in range(2, k):
    negafib_pos[i] = negafib_pos[i - 1] + negafib_pos[i - 2]
    negafib_neg[i] = negafib_neg[i - 2] - negafib_neg[i - 1]
negafib_neg.pop(0)
negafib_neg.reverse()
negafib = negafib_neg + negafib_pos
print (negafib)

# сделать ряд фиб для положительных чисел добавляя значения 

# Задача №3. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.

# list =  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, 
# {" V ":"S009"}, {"VIII":"S007"}]
# values_list = []
# for el in list:
#     n = el.values()
#     values_list.append(*n)
# print (values_list)
# values_list = set(values_list)
# print (f'The list of unique values is: {values_list}')