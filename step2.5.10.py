"""
Напишите программу, на вход которой подаётся список чисел одной строкой.
Программа должна для каждого элемента этого списка вывести сумму двух его соседей.
Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий на противоположном
конце этого списка. Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7"
(без кавычек).

Если на вход пришло только одно число, надо вывести его же.

Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
"""
a = [int(y) for y in input().split()]
N = len(a)
b = [1]*N

if N == 0:
    b = [0]
elif N == 1:
    b = a
else:
    for i in range(0,N-1):
        b[i] = a[i-1] + a[i+1]
    b[N-1] = a[N-2] + a[0]

for j in b:
    print(j, end=' ')