# досрок

for file in (r"D:\Downloads\27-A (6).txt", r"D:\Downloads\27-B (6).txt"):
    with open(file) as f:
        n = int(f.readline())

        mas = list(map(int, f.readlines()))
        s = [0]*n
        k = b = 0
        for i in range(1, n//2 + 1):
            s[0] += mas[i]*i
            k += mas[i]

        for i in range(0, n//2):
            s[0] += i*mas[-i%n]
            b += mas[-i%n]
        res = 0
        for i in range(1, n):
            s[i] = s[i-1] + b - k
            b = b + mas[i] - mas[(i + n//2)%n]
            k = k - mas[i] + mas[(i + n//2)%n]
            if s[res] > s[i]:
                res = i
        print(res + 1)
