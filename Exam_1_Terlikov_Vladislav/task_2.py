"""
2.	Написать программу для вычисления значения выражений.
 Проверить правильность выполнения задания с помощью тестовых значений.
"""
import math

a = int(input("Введите значение: а = "))
b = int(input("Введите значение: b = "))
y = int(input("Введите значение: y = "))
y = 0.25 * (math.sin(a + b - y) + math.sin(b + a - y)
            + math.sin(y + a - b) - math.sin(a + b + y))
print(y)