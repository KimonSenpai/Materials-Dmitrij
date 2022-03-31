from math import ceil
f = open("D:\\Downloads\\27-B (2).txt", 'r')
n = int(f.readline())
mas = [0]*10001

res = 0
for line in f:
    val = int(line)

    for i in range(ceil(val/2)):
        res += mas[i]*mas[val - i]
    #val == 9, val//2 == 4
    #val == 10, val//2 == 5
    if val%2 == 0:
        res += mas[val//2]*(mas[val//2] - 1)//2

    mas[val] += 1
print(res)