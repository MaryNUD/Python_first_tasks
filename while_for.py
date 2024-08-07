'''Задача №1. По данному целому неотрицательному n вычислите значение n!. 
N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
Решить задачу используя цикл while Input: 5 Output: 120'''

'''
print ('Enter your number to count its factorial:')
n = int(input())
if n < 0:
    print ('You entered a negative number')
result = 1
i = 1
while i <= n:
    if n == 0:
        print (result)
    else:
        result = result * i
        i += 1
        print (result)
'''

'''Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
то есть выведите такое число n, что φ(n)=A. 
Если А не является числом Фибоначчи, выведите число -1. Input: 5 Output: 6'''

'''
print ('Enter your number (> 0):')
n = int(input())
first = 0
second = 1
current = first + second
i = 3 # the positions of the fibonnachi's number (current)
# checking
if n <= 0:
    print ('Check your number')
elif n == 1:
     print ('The position of your number is 2 or 3')
# cycle
while current < n:
    first = second
    second = current
    current = first + second
    i += 1
    if current > n:
        print (-1)
    elif current == n:
        print ('The position of your number is', i)
'''

