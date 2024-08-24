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