'''print (1)
n = None
m = 123
print (n, m)'''

'''print ('Enter the value of the variable r')
r = input()
# print (r)
print (type(r))'''

'''a = 3
b = 11
s = 2022
print (a, b, s)
# интерполяция
print ('{} - {} - {}'.format(a,b,s))
print (f'first - {a} second - {b} third - {s}')'''

'''n = 1.345
print (n * 2)
print (int(n))
m = '234'
print (m * 2)
print (int(m) * 2)'''

'''inter = 6
print (inter)
inter += 3
print (inter)
inter -= 2 
print (inter)
inter **= 2
print (inter)'''

'''a = 1 < 3
print (a)
b = 5 > 6
print (b)
c = a and b
print (c)
c = a or b
print (c)'''

'''print ('Enter username')
username = input()
if username == 'Mary':
    print ('Glad to see you, Mary!')
else: 
    print ('Sorry, you cannot enter!')'''

'''n = 85
while n >= 5:
    n //= 5
print (n)'''

'''n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0: # если остаток при делении числа n на i равен 0
        flag = False
        print(i)
    elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
        print(n)
        flag = False
    i += 1'''

'''r = range (1, 10, 2)
for i in r:
    print (i)
for i in 'Mary':
    print (i)'''

'''text = 'True LoVe exiSts, believe me!'
print (len(text))
print ('love' in text)
print ('Falling' in text)
print(text.lower())
print(text.upper())
print(text.replace('LoVe', 'LOVE'))'''
       