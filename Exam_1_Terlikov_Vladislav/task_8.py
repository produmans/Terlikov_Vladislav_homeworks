"""
8.	Вам передан массив чисел.
 Известно, что каждое число в этом массиве имеет пару,
  кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
"""
lst = [1, 5, 2, 9, 2, 9, 1]
for i in lst:
    if lst.count(i) == 1:
        print(i)