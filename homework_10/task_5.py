"""
5) Создайте 2 множества:
- Если они одинаковые: вывести что они равны
- Если 1 множество полностью состоит из второго: вывести сообщение множество 1 состоит из множества2
- Если 2 множество полностью состоит из 1: вывести сообщение множество 2 состоит из множества 1
"""
set1 = {1, 2, 3}
set2 = {4, 5, 6, 1, 2, 3}
if set1 == set2:
    print('Множества равны')
elif set1.issubset(set2):
    print('ммножество 1 состоит из множества 2')
elif set2.issubset(set1):
    print('множество 2 состоит из множества 1')