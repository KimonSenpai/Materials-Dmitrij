f = open("D:\\Downloads\\27B (1).txt", 'r')
n = int(f.readline())

mas = [int(val) for val in f]

pre = [[0]*3 for _ in range(2)]

# pre[i][j] - кол-во чисел с остатком от делени на 3 равном j
# и четностью префикса i
pref = (mas[0] + mas[1])%2 == 1
pref2 = False
res = 0
for i in range(2, n):
    if mas[i-2] % 2 == 1:
        pref2 = not pref2
    pre[int(pref2)][mas[i-2]%3] += 1

    res += pre[int(pref)][-mas[i]%3]

    if mas[i]%2 == 1:
        pref = not pref
print(res)