"""
Требуется определить, является ли данный год високосным.

Напомним, что високосными годами считаются те годы, порядковый номер которых либо кратен 4,
но при этом не кратен 100, либо кратен 400 (например, 2000-й год являлся високосным, а 2100-й будет невисокосным годом).
"""
n = int(input())
if n % 4 == 0 and (n % 100 != 0 or n % 400 == 0):
    print('Високосный')
else: print('Обычный')