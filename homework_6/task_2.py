"""
Даны 2 списка:a=[4,6,'pу','tell',78] b=[44,'hello’,56,'exept’,3]
Выполнить следующие операции: 1)Сложить два списка 2) Добавьте элемент 6 на 3 позицию.
3)Удалите все текстовые переменные 4) Посчитайте количество элементов списка
"""
a = [4, 6, 'pу', 'tell', 78]
b = [44, 'hello', 56, 'exept', 3]
c = a + b
c.insert(3, 6)
for i in c:
    if type(i) == str:
        c.remove(i)
print(c)
x = len(c)
print(f'{x}:количество элементов списка')