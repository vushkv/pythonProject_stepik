"""
Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке,
и после первого введенного нуля выводит сумму полученных на вход чисел.
"""
c = int (input())
s = 0
while c != 0:
    s = s + c
    c = int (input())
print (s)