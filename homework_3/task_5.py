"""Пользователь вводит три числа.
Если все числа больше 10, то вывести на экран yes
 , иначе no"""

x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
z = int(input('Введите третье число: '))
if x > 10 and y > 10 and z > 10:
    print('yes')
else:
    print('no')
