# 3. Дана следующая функция
"""y = f(x).

y = 2x – 10, если x > 0

y = 0, если x = 0

y = 2 *|x| - 1, если x < 0"""

x = int(input('Введите число: '))
if x > 0:
    y = 2 * x - 10
    print(y)
elif x == 0:
    y = 0
    print(y)
else:
    y = 2 * abs(x) - 1
    print(y)
    