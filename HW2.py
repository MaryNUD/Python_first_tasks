'''Задание 1: Поставьте оценку!
Напишите программу, которая находит количество положительных и количество
отрицательных чисел в последовательности. Последовательность заканчивается на
числе 0.'''

'''n = int(input('Enter your mark from -100 to 100 for this app:'))
pos = 0
neg = 0
while n != 0:
    if n > 0:
        pos += 1
    else:
        neg += 1
    n = int(input('Enter your mark from -100 to 100 for this app:'))    
print ('Overall number of positive marks', pos)
print ('Overall number of positive marks', neg)'''

'''Задача 2. Обычный день на работе
Максим программирует целый день на работе и вечером идёт домой. Каждый час
начальство кидает ему несколько задач, которые нужно решить до следующего
рабочего часа. Вдобавок каждый час Максиму звонит супруга. Он знает, что если он
возьмёт трубку, то жена попросит зайти вечером в магазин.
Напишите программу, в которой считается, сколько задач выполнил Максим за день
(восемь часов). Если он хотя бы раз взял трубку, то в конце дополнительно выводите
сообщение: «Нужно зайти в магазин».'''

'''h = 1
tasks_sum = 0
shop = False
while h <= 8:
    print (h, 'hour')
    tasks = int(input('Enter the number of solved tasks:'))
    tasks_sum += tasks
    call = int(input('Wife is calling (if he takes the phone enter 1, else enter 0):'))
    if call == 1:
        shop = True
    h += 1
print ('Overall number of solved tasks is', tasks_sum)
if shop:
    print ('You have to go to the shop')
else:
    print ('You do not need to go to the shop')'''

'''Задача 3. Игра «Угадай число»
Папа-программист написал для сына программу, которая просит его угадать
число. Недостаток программы был в том, что бедному сыну приходилось её
каждый раз перезапускать, чтобы угадывать число. Теперь, когда мы знаем
гораздо больше, пришло время исправить этот недостаток и заодно немного
улучшить саму игру.
Напишите программу-игру, которая запрашивает у пользователя число до тех
пор, пока он его не отгадает. Выводите сообщения в соответствии с примером.'''

'''guess_n = 13 
print ('Guess the number from 0 to 20')
try_sum = 0
while True:
    try_sum += 1
    n = int(input('Enter your number:'))
    if n < guess_n:
        print ('Your number is smaller then ours. Try again!')
    elif n > guess_n:
        print ('Your number is bigger then ours. Try again!')
    elif n == guess_n:
        print ('You are right! The number we chose is', guess_n)
        break
print ('The number of tries is', try_sum)'''

'''Задача 4. Посчитай чужую зарплату...
Бухгалтер устала постоянно считать вручную среднегодовую зарплату
сотрудников компании и, чтобы облегчить себе жизнь, обратилась к
программисту.
Напишите программу, которая принимает от пользователя зарплату сотрудника
за каждый из 12 месяцев и выводит на экран среднюю зарплату за год.'''

'''month = 1
sum = 0
while month <= 12:
    print ('Month', month, 'salary:')
    salary = int(input())
    sum += salary
    month += 1
print ('Average annual salary is', sum / 12)'''

'''Задача 5. Пропавшая карточка
Для настольной игры используются карточки с номерами от 1 до N. Одна
карточка потерялась. Напишите программу, которая поможет найти потерянную
карточку, если номера оставшихся известны. Найдите её, зная номера
оставшихся карточек.
Введите число карточек — N.
Затем введите N − 1 номера оставшихся карточек. Они могут быть введены в
любом порядке.'''

'''total_c = int(input('Enter an overall number of cards:'))
total_sum = 0
for card in range (1, total_c + 1):
    total_sum += card
for remaining_card in range (total_c -1):
    remaining_card = int(input('Enter the number of a remaining card:'))
    total_sum -= remaining_card
print ('The number of the lost card is', total_sum)'''
