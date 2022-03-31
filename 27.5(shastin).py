for path in ("D:\\Downloads\\27a (4).txt", "D:\\Downloads\\27b (4).txt"):
    f = open(path)

    n, K, D = (int(v) for v in f.readline().split())

    mas = [int(line) for line in f]

    pref = [[10**10 for i in range(D)] for j in range(K)]
    
    ost = sum(mas) % D
    pr = 0
    max_s = 0
    for i in range(n):
        pr += mas[i]
        max_s = max(max_s, pr - pref[pr % K][(pr - ost) % D])#pr - x = ost (mod D) => x = (pr - ost)%D
        pref[pr % K][pr % D] = min(pref[pr % K][pr % D], pr)
    print(max_s, end=' ')

print()