# 2592 kompege


# x = 2^p * q^4, q in P
# y = p^n * q^m нечетных делителей: (n + 1)*(m + 1)

def check(v):
    div = 2
    while div*div <= v:
        if v % div == 0:
            return False
        div += 1
        
    return True

a = 55000000
b = 60000000
q = 3
res = []
while q**4 <= b:
    if not check(q):
        q += 1
        continue
    p = 0
    while 2**p * q**4 <= b:
        vv = 2**p * q**4
        if vv >= a:
            res += [(vv, q**4)]
        p += 1

    q += 1

res.sort()
for l in res:
    print(*l)