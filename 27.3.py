# Дана последовательность. Найти максимальную сумму пары чисел, разность индексов 
# в последовательности у которых не менее 7. Числа натуральные.


f = open("27.txt", 'r')
n = int(f.readline())

mas = [0]*7

max_val = -1
max_sum = -1

for i in range(7):
    mas[i] = int(f.readline())

for i in range(7, n):
    val = int(f.readline())

    max_val = max(max_val, mas[i%7])
    max_sum = max(max_sum, max_val + val)

    mas[i%7] = val

print(max_sum)
