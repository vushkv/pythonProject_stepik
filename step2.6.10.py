"""
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк.
После последней строки матрицы идёт строка, содержащая только строку "end" (без кавычек, см. Sample Input).

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов
первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится
с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
"""
n = ''
m = []
while True:
    n = str(input()) # ввод строк
    if n == 'end':
        break
    m.append([int(s) for s in n.split()])
li, lj = len(m), len(m[0])
new = [[sum([m[i - 1][j], m[(i + 1)%li][j], m[i][j - 1], m[i][(j + 1) % lj]]) for j in range(lj)] for i in range(li)]

for i in range (li):
    for j in range (lj):
        print(new[i][j], end =' ')
    print()